from django import forms
from django.contrib.auth.models import User
from .models import Profile
from .models import Blog
from ckeditor.widgets import CKEditorWidget  # Importar el widget de CKEditor

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True)  # Hacer obligatorio el email
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'description', 'website']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']  # Nombre, email y contraseña
        widgets = {
            'password': forms.PasswordInput(),  # Para ocultar la contraseña
        }


class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())  # Aplicar CKEditor

    class Meta:
        model = Blog
        fields = ['title', 'subtitle', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
        }