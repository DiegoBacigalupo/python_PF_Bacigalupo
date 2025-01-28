from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)  # Biografía del usuario
    location = models.CharField(max_length=100, blank=True)  # Ubicación
    birthdate = models.DateField(null=True, blank=True)  # Fecha de nacimiento

    def __str__(self):
        return self.user.username
    

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=300, verbose_name="Subtítulo")
    content = models.TextField(verbose_name="Cuerpo")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    image = models.ImageField(upload_to='blog_images/', verbose_name="Imagen")

    def __str__(self):
        return self.title
    
image = models.ImageField(upload_to='blog_images/', default='default_image.jpg', verbose_name="Imagen")