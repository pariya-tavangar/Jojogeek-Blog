from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all/', views.all_posts, name='all_posts'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('about/', views.about, name="about"),
]
# This code defines the URL patterns for a Django blog application. It includes two URL patterns: