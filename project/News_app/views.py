from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Articles
from .forms import ArticlesForm, ArticlesCrForm, NewsCrForm
from .filters import ArticlesFilter
from django.urls import reverse_lazy
from .models import Category, Post


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


class ArticlesCreate(CreateView):
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


class ArticlesEdit(UpdateView):
    form_class = ArticlesCrForm
    model = Post
    context_object_name = 'articles_edit'
    template_name = 'flatpages/edit.html'
    success_url = reverse_lazy('articles_list')


class NewsEdit(UpdateView):
    form_class = NewsCrForm
    model = Post
    context_object_name = 'news_edit'
    template_name = 'flatpages/edit.html'
    success_url = reverse_lazy('articles_list')


class NewsDelete(DeleteView):
    model = Articles
    template_name = 'flatpages/delete.html'
    success_url = reverse_lazy('articles_list')


class ArticlesDelete(DeleteView):
    model = Articles
    template_name = 'flatpages/delete.html'
    success_url = reverse_lazy('articles_list')

