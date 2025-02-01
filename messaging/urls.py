from django.urls import path
from . import views

urlpatterns = [
    path('public/', views.public_messages, name='public_messages'),
    path('private/', views.private_messages, name='private_messages'),
    path('send/', views.send_message, name='send_message'),
]