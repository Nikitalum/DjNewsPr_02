from django.urls import path
from . import views
from .views import ArticlesList, ArticlesDetail, search_news, multiply

urlpatterns = [
    path('', views.hello),
    path('news/search/', views.search_news, name='search'),
    path('news/', ArticlesList.as_view(), name='articles_list'),
    path('<int:pk>', ArticlesDetail.as_view(), name='articles_detail'),
    path('multiply/', multiply),
]