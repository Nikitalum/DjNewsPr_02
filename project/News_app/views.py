from django.shortcuts import render
from django.views.generic import ListView
from .models import Articles
from django.http import HttpResponse


# def index(request):
#     return render(request, 'flatpages/news.html')

#
def news(request):
    news = Articles.objects.order_by("-date")
    return render(request, 'flatpages/news.html', news)


class ArticlesList(ListView):
    model = Articles
    ordering = 'date'
    template_name = 'flatpages/news.html'
    context_object_name = 'articles'
    paginate_by = 1


