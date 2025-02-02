from django import forms
from messaging.models import Message
from django.contrib.auth.models import User

class MessageForm(forms.ModelForm):
    is_public = forms.BooleanField(required=False, label="Mensaje público: Marcar si deseas que este mensaje sea público.")

    class Meta:
        model = Message
        fields = ["receiver", "content", "is_public"]