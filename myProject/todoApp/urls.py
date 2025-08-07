from django.urls import path
from . import views

urlpatterns = [
    path('', views.FirstView, name='index'),
    path('home', views.HomeView, name='home'),
    path('register/', views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
]
