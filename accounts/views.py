from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import BlogForm
from .models import Blog


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guardar el usuario
            # Crear el perfil para el usuario
            Profile.objects.create(user=user)
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    user_blogs = Blog.objects.filter(author=request.user)  # Obtener los blogs del usuario

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
    else:
        profile_form = ProfileForm(instance=profile)

    return render(request, 'accounts/profile.html', {
        'profile_form': profile_form,
        'user_blogs': user_blogs
    })

@login_required
def welcome(request):
    return render(request, 'accounts/welcome.html')

@login_required
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user  # Asociar el blog al usuario autenticado
            blog.save()
            return redirect('all_blogs')  # Redirige a la página de todos los blogs
    else:
        form = BlogForm()
    return render(request, 'accounts/add_blog.html', {'form': form})


def all_blogs(request):
    blogs = Blog.objects.all().order_by('-created_at')  # Ordenar por fecha de creación
    return render(request, 'accounts/all_blogs.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'accounts/blog_detail.html', {'blog': blog})