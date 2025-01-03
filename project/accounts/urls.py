from django.urls import path
from .views import SignUp
from . import views

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]