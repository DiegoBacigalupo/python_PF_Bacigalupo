from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)  # Biografía del usuario
    location = models.CharField(max_length=100, blank=True)  # Ubicación
    birthdate = models.DateField(null=True, blank=True)  # Fecha de nacimiento

    def __str__(self):
        return self.user.username