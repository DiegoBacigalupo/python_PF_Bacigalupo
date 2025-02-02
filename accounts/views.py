from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Profile
from .forms import BlogForm
from .models import Blog
from django.views.generic import ListView
from django.views.generic import DetailView

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Guardar sin confirmar
            user.set_password(form.cleaned_data["password"])  # Encriptar la contraseña
            user.save()  # Ahora sí lo guardamos
            
            # Autenticar al usuario
            user = authenticate(username=user.username, password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)  # Iniciar sesión automáticamente
                return redirect('welcome')  # Redirigir a la página de inicio o perfil

    else:
        form = UserRegisterForm()

    return render(request, "accounts/register.html", {"form": form})

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)  # Crea si no existe
    user_blogs = Blog.objects.filter(author=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
    else:
        profile_form = ProfileForm(instance=profile)

    return render(request, 'accounts/profile.html', {
        'profile': profile,  # <-- Aquí pasamos el perfil al contexto
        'profile_form': profile_form,
        'user_blogs': user_blogs
    })

@login_required
def welcome(request):
    return render(request, 'accounts/welcome.html')

@login_required
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('all_blogs')
    else:
        form = BlogForm()

    return render(request, 'accounts/add_blog.html', {'form': form})


class BlogListView(ListView):
    model = Blog
    template_name = 'accounts/all_blogs.html'
    context_object_name = 'blogs'
    ordering = ['-created_at']

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'accounts/blog_detail.html'
    context_object_name = 'blog'

def about(request):
    return render(request, 'accounts/about.html')