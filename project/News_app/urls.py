from django.urls import path
from . import views
from .views import ArticlesList, ArticlesDetail, ArticlesSearch, search_news, multiply

urlpatterns = [
    path('', views.hello),
    path('news/search/', ArticlesSearch.as_view(), name='search'),
    path('news/', ArticlesList.as_view(), name='articles_list'),
    path('<int:pk>', ArticlesDetail.as_view(), name='articles_detail'),
    path('multiply/', multiply),
]