from django.shortcuts import render
from django.views.generic import ListView
from .models import Articles


class ArticlesList(ListView):
    model = Articles
    template_name = 'flatpages/news.html'
    context_object_name = 'articles'
