from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm

@login_required
def public_messages(request):
    """Muestra todos los mensajes públicos"""
    messages = Message.objects.filter(receiver__isnull=True).order_by('-timestamp')
    return render(request, 'messaging/public_messages.html', {'messages': messages})

@login_required
def private_messages(request):
    """Muestra los mensajes privados recibidos por el usuario"""
    messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'messaging/private_messages.html', {'messages': messages})


@login_required
def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            if not message.receiver:
                message.receiver = None  # Asegúrate de que sea NULL si no hay receptor
            message.save()
            return redirect('welcome')  # Redirige donde corresponda
    else:
        form = MessageForm()

    return render(request, 'messaging/send_message.html', {'form': form})
