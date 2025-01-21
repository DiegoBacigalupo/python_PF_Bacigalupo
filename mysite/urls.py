"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Ruta a la página de inicio
    path('accounts/', include('accounts.urls')),  # Esto ya estaba, pero necesitas agregar las URLs de auth
    path('accounts/', include('django.contrib.auth.urls')),  # Agrega esto para las vistas de login/logout/password_reset, etc.
    path('', include('blog.urls')),  # Esto agrega las rutas de 'blog'
]
