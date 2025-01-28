
from django.contrib import admin
from .models import Blog, Profile  # Importa el modelo que quieras administrar

admin.site.register(Blog) 
admin.site.register(Profile) 
