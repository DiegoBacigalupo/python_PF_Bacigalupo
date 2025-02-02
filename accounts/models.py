from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='profile_pics/default.jpg', null=True, blank=True)
    description = models.TextField(blank=True)  # Agregamos la descripción
    website = models.URLField(blank=True, null=True)  # Agregamos el link a la web

    def __str__(self):
        return self.user.username
    


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=300, verbose_name="Subtítulo")
    content = models.TextField(verbose_name="Cuerpo")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    
image = models.ImageField(upload_to='blog_images/', default='default_image.jpg', verbose_name="Imagen")