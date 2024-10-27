from django.urls import path
from .views import ArticlesList

urlpatterns = [
    path('', ArticlesList.as_view())
]