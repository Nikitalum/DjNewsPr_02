from django.urls import path
from . import views
from .views import ArticlesList

urlpatterns = [
    # path('', views.news)
    path('', ArticlesList.as_view(), name='articles_list')
]