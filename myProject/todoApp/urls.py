from django.urls import path
from . import views

urlpatterns = [
    path('', views.FirstView, name='index'),
    path('home', views.HomeView, name='home'),
    path('register/', views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'),
]
