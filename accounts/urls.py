from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add-blog/', views.add_blog, name='add_blog'),
    path('all-blogs/', views.all_blogs, name='all_blogs'),
]