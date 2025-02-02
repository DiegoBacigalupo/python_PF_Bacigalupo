from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm
from django.db.models import Q
@login_required
def public_messages(request):
    """Muestra todos los mensajes públicos"""
    messages = Message.objects.filter(is_public=True).order_by('-timestamp')
    return render(request, 'messaging/public_messages.html', {'messages': messages})

@login_required
def private_messages(request):
    """Muestra los mensajes privados enviados y recibidos por el usuario"""
    messages_received = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    messages_sent = Message.objects.filter(sender=request.user).order_by('-timestamp')

    return render(request, 'messaging/private_messages.html', {
        'messages_received': messages_received,
        'messages_sent': messages_sent
    })


@login_required
def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user

            if form.cleaned_data["is_public"]:  # 🔹 Si es público, no tiene receptor
                message.receiver = None
            elif not message.receiver:  # 🔹 Evitar que se envíe sin receptor si no es público
                return render(request, "messaging/send_message.html", {"form": form, "error": "Debes seleccionar un receptor o marcarlo como público."})

            message.save()
            return redirect("public_messages" if message.is_public else "private_messages")

    else:
        form = MessageForm()

    return render(request, "messaging/send_message.html", {"form": form})