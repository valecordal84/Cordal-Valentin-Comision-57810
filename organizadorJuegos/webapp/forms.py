from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
 
class WishlistForm(forms.ModelForm):
    class Meta:
        model = wishlist
        fields = ['nombre', 'plataforma', 'genero', 'multijugador', 'solitario']
        
class PlataformasForm(forms.ModelForm):
    class Meta:
        model= plataformas
        fields= ['nombrePlataforma', 'membresia']
        
class JCForm(forms.ModelForm):
    class Meta:
        model= juegosComprar
        fields= ['nombre', 'plataforma', 'precio', 'multijugador', 'solitario']
        
class JTForm(forms.ModelForm):
    class Meta:
        model= juegosTerminados
        fields= ['nombre', 'plataforma', 'genero', 'recomiendo']
        
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita su contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model =  User
        fields = ["username", "email", "password1", "password2"]
        
        
class editarPerfilForm(UserChangeForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField (label = "nombre", max_length=255, required=True)
    last_name = forms.CharField (label = "apellido", max_length=255, required=True)
    class Meta:
        model =  User
        fields = ["email","first_name", "last_name"]
        
        
class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)
    
    