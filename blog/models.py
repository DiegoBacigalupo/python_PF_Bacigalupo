from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # Título de la publicación
    content = models.TextField()  # Contenido de la publicación
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de la última actualización

    def __str__(self):
        return self.title

