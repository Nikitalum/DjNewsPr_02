from django.urls import path
from . import views
from .views import ArticlesList, ArticlesDetail, ArticlesSearch, ArticlesCreate, NewsCreate, multiply, NewsEdit, ArticlesEdit
urlpatterns = [
    path('', views.hello),
    path('news/search/', ArticlesSearch.as_view(), name='search'),
    path('news/', ArticlesList.as_view(), name='articles_list'),
    path('<int:pk>', ArticlesDetail.as_view(), name='articles_detail'),
    path('news/<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
    path('articles/<int:pk>/edit/', ArticlesEdit.as_view(), name='articles_edit'),
    path('multiply/', multiply),
    path('articles/create', ArticlesCreate.as_view(), name='articles_create'),
    path('news/create', NewsCreate.as_view(), name='news_create')
]