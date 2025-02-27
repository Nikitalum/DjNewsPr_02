from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Articles, Subscriber
from .forms import ArticlesForm, ArticlesCrForm, NewsCrForm
from .filters import ArticlesFilter
from django.urls import reverse_lazy
from .models import Category, Post, Subscriber
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.db.models import Exists, OuterRef


def hello(request):
    return render(request, 'flatpages/hello.html')


def search(request):
    return render(request, 'flatpages/search.html')


def search_news(request):
    form = ArticlesForm
    return render(request, 'flatpages/search.html', {'form': form})


def news(request):
    news = Articles.objects.order_by("-date")
    return render(request, 'flatpages/news.html', news)


class ArticlesList(ListView):
    model = Post
    ordering = 'id'
    template_name = 'flatpages/news.html'
    context_object_name = 'articles'
    paginate_by = 10


class ArticlesSearch(ListView):
    model = Post
    ordering = 'date'
    template_name = 'flatpages/search.html'
    context_object_name = 'articles'
    paginate_by = 8

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ArticlesFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ArticlesDetail(DetailView):
    model = Post
    template_name = 'flatpages/news_detail.html'
    context_object_name = 'article'


class ArticlesCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('News_app.add_post',)
    form_class = ArticlesCrForm
    model = Post
    template_name = 'flatpages/add.html'
    success_url = reverse_lazy('articles_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/articles/create':
            post.type = 'A'
        post.save()
        return super().form_valid(form)


class ArticlesEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('News_app.change_post',)
    form_class = ArticlesCrForm
    model = Post
    context_object_name = 'articles_edit'
    template_name = 'flatpages/edit.html'
    success_url = reverse_lazy('articles_list')


class NewsEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('News_app.change_post',)
    form_class = NewsCrForm
    model = Post
    context_object_name = 'news_edit'
    template_name = 'flatpages/edit.html'
    success_url = reverse_lazy('articles_list')


class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('News_app.delete_post',)
    model = Post
    template_name = 'flatpages/delete.html'
    context_object_name = 'articles'
    success_url = reverse_lazy('articles_list')


class ArticlesDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('News_app.delete_post',)
    model = Post
    template_name = 'flatpages/delete.html'
    context_object_name = 'articles'
    success_url = reverse_lazy('articles_list')


class CategoryListView(ArticlesList):
    model = Post
    template_name = 'flatpages/subscriptions.html'
    context_object_name = 'category_news_list'
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, id = self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category).order_by('-date')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['in_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context

@login_required
@csrf_protect
def subscribe(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscriber.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscriber.objects.filter(
                user=request.user,
                category=category,
            ).delete()

    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(
            Subscriber.objects.filter(
                user=request.user,
                category=OuterRef('pk'),
            )
        )
    ).order_by('name')
    return render(
        request,
        'flatpages/subscriptions.html',
        {'categories': categories_with_subscriptions},
    )