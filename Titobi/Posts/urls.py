from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name= 'home'),
    path('featured items/', views.featured_items, name= 'featured items'),
    path('about/', views.about, name= 'about'),
    path('order/', views.Order, name= 'order'),
    path('auth/admin/manage posts/', views.manage_posts, name= 'manage posts'),
    path('auth/admin/manage posts/new post', views.new_post, name= 'new post'),
    path('accounts/login/', views.login_view, name= 'login'),
    path('accounts/login/', views.logout_view, name= 'logout'),
]