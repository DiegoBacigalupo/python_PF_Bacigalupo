from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")  # Usuario que envía el mensaje
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages", null=True, blank=True)  # Usuario que recibe el mensaje (null si es público)
    content = models.TextField(verbose_name="Contenido")
    timestamp = models.DateTimeField(auto_now_add=True)  # Fecha y hora del mensaje

    def is_public(self):
        return self.receiver is None  # Si no hay receptor, el mensaje es público

    def __str__(self):
        return f"De {self.sender.username} para {self.receiver.username if self.receiver else 'Todos'}"