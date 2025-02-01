from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import BlogListView, BlogDetailView
from django.urls import include
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add-blog/', views.add_blog, name='add_blog'),
    path('blogs/', BlogListView.as_view(), name='all_blogs'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('about/', views.about, name='about'),
    path('messages/', include('messaging.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)