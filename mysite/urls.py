from django.contrib import admin
from django.urls import path, include
from blog import views
from accounts import views as accounts_views
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Página de inicio
    path('', accounts_views.welcome, name='home'),   
    
    # URLs de autenticación y cuentas
    path('accounts/', include('accounts.urls')),  # URLs de la app accounts
    path('accounts/', include('django.contrib.auth.urls')),  # URLs de autenticación predefinidas de Django

    # URLs de la aplicación blog
    path('blog/', include('blog.urls')),  # Se cambia '' por 'blog/' para evitar conflictos
    
]