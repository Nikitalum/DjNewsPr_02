from django.urls import path
from . import views
from .views import ArticlesList, ArticlesDetail, ArticlesSearch, ArticlesCreate, \
    NewsEdit, ArticlesEdit, NewsDelete, ArticlesDelete, subscribe, CategoryListView
urlpatterns = [
    path('', views.hello, name='about'),
    path('news/search/', ArticlesSearch.as_view(), name='search'),
    path('news/', ArticlesList.as_view(), name='articles_list'),
    path('<int:pk>', ArticlesDetail.as_view(), name='articles_detail'),
    path('news/<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/<int:pk>/edit/', ArticlesEdit.as_view(), name='articles_edit'),
    path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),
    path('articles/create', ArticlesCreate.as_view(), name='articles_create'),
    path('news/create', ArticlesCreate.as_view(), name='news_create'),
    path('news/categories/<int:pk>', CategoryListView.as_view(), name = 'category_list'),
    path('news/categories/<int:pk>/subscribe',subscribe, name='subscribe')
]