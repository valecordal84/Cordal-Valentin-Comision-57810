from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Principales views
def home(request):
    return render (request,"webapp/index.html")

@login_required
def wl(request):
    contexto = {"wishlist": wishlist.objects.all()}
    return render (request, "webapp/wishlist.html", contexto)

@login_required
def plataforma(request):
    contexto = {"plataformas": plataformas.objects.all()}
    return render (request, "webapp/plataformas.html", contexto)

@login_required
def jc(request):
    contexto = {"juegosComprar": juegosComprar.objects.all()}
    return render (request, "webapp/juegosComprar.html", contexto)

@login_required
def jt(request):
    contexto = {"juegosTerminados": juegosTerminados.objects.all()}
    return  render (request, "webapp/juegosTerminados.html", contexto)

@login_required
def acercaDeMi(request):
    return render (request, "webapp/acercaDeMi.html")



#Formularios para añadir elementos

@login_required
def wishlistForm(request):
    if request.method == "POST":
        miForm = WishlistForm(request.POST)
        if miForm.is_valid():
            wishlist_nombre = miForm.cleaned_data.get("nombre")
            wishlist_plataforma = miForm.cleaned_data.get("plataforma")
            wishlist_genero = miForm.cleaned_data.get("genero")
            wishlist_multijugador = miForm.cleaned_data.get("multijugador")
            wishlist_solitario = miForm.cleaned_data.get("solitario")
            wishlist_item = wishlist(
                nombre=wishlist_nombre,
                plataforma=wishlist_plataforma,
                genero=wishlist_genero,
                multijugador=wishlist_multijugador,
                solitario=wishlist_solitario
            )
            wishlist_item.save()
            return redirect('wishlist')
    else:
        miForm = WishlistForm()
        
    return render(request, "webapp/wishlistForm.html", {"form": miForm})

@login_required
def plataformasForm(request):
    if request.method == "POST":
        miForm = PlataformasForm(request.POST)
        if miForm.is_valid():
            plataforma_nombre = miForm.cleaned_data.get("nombrePlataforma")
            plataforma_membresia = miForm.cleaned_data.get("membresia")
            plataforma_item = plataformas(
                nombrePlataforma=plataforma_nombre,
                membresia=plataforma_membresia,
            )
            plataforma_item.save()
            return redirect('plataformas')
    else:
        miForm = PlataformasForm()
        
    return render(request, "webapp/plataformasForm.html", {"form": miForm})

@login_required
def jcForm(request):
    if request.method == "POST":
        miForm = JCForm(request.POST)
        if miForm.is_valid():
            jc_nombre = miForm.cleaned_data.get("nombre")
            jc_plataforma = miForm.cleaned_data.get("plataforma")
            jc_precio = miForm.cleaned_data.get("precio")
            jc_multijugador = miForm.cleaned_data.get("multijugador")
            jc_solitario = miForm.cleaned_data.get("solitario")
            jc_item = juegosComprar(
                nombre=jc_nombre,
                plataforma=jc_plataforma,
                precio=jc_precio,
                multijugador=jc_multijugador,
                solitario=jc_solitario,
            )
            jc_item.save()
            return redirect('juegosComprar')
    else:
        miForm = JCForm()
        
    return render(request, "webapp/jcForm.html", {"form": miForm})

@login_required
def jtForm(request):
    if request.method == "POST":
        miForm = JTForm(request.POST)
        if miForm.is_valid():
            jt_nombre = miForm.cleaned_data.get("nombre")
            jt_plataforma = miForm.cleaned_data.get("plataforma")
            jt_genero = miForm.cleaned_data.get("genero")
            jt_recomiendo = miForm.cleaned_data.get("recomiendo")
            jt_item = juegosTerminados(
                nombre=jt_nombre,
                plataforma=jt_plataforma,
                genero=jt_genero,
                recomiendo=jt_recomiendo,
            )
            jt_item.save()
            return redirect('juegosTerminados')
    else:
        miForm = JTForm()
        
    return render(request, "webapp/jtForm.html", {"form": miForm})


#Formularios para actualizar elementos

@login_required
def wishlistUpdate(request, nombre_wishlist):
    wishlist_item = get_object_or_404(wishlist, nombre=nombre_wishlist)
    
    if request.method == "POST":
        form = WishlistForm(request.POST, instance=wishlist_item)
        if form.is_valid():
            form.save()
            return redirect('wishlist')
    else:
        form = WishlistForm(instance=wishlist_item)
        
    return render(request, "webapp/wishlistForm.html", {"form": form})

@login_required
def plataformasUpdate(request, nombre_plataforma):
    plataforma_item = get_object_or_404(plataformas, nombrePlataforma=nombre_plataforma)
    
    if request.method == "POST":
        form = PlataformasForm(request.POST, instance=plataforma_item)
        if form.is_valid():
            form.save()
            return redirect('plataformas')
    else:
        form = PlataformasForm(instance=plataforma_item)
        
    return render(request, "webapp/plataformasForm.html", {"form": form})

@login_required
def jcUpdate(request, nombre_jc):
    jc_item = get_object_or_404(juegosComprar, nombre=nombre_jc)
    
    if request.method == "POST":
        form = JCForm(request.POST, instance=jc_item)
        if form.is_valid():
            form.save()
            return redirect('juegosComprar')
    else:
        form = JCForm(instance=jc_item)
        
    return render(request, "webapp/jcForm.html", {"form": form})

@login_required
def jtUpdate(request, nombre_jt):
    jt_item = get_object_or_404(juegosTerminados, nombre=nombre_jt)
    
    if request.method == "POST":
        form = JTForm(request.POST, instance=jt_item)
        if form.is_valid():
            form.save()
            return redirect('juegosTerminados')
    else:
        form = JTForm(instance=jt_item)
        
    return render(request, "webapp/jtForm.html", {"form": form})


#Formularios de Delete de datos

@login_required
def wishlistDelete(request, nombre_wishlist):
    wishlist_item = get_object_or_404(wishlist, nombre=nombre_wishlist)
    wishlist_item.delete()
    return redirect('wishlist')

@login_required
def plataformasDelete(request, nombre_plataforma):
    plataforma_item = get_object_or_404(plataformas, nombrePlataforma=nombre_plataforma)
    plataforma_item.delete()
    return redirect('plataformas')

@login_required
def jcDelete(request, nombre_jc):
    jc_item = get_object_or_404(juegosComprar, nombre=nombre_jc)
    jc_item.delete()
    return redirect('juegosComprar')

@login_required
def jtDelete(request, nombre_jt):
    jt_item = get_object_or_404(juegosTerminados, nombre=nombre_jt)
    jt_item.delete()
    return redirect('juegosTerminados')


# Formulario de Registros

def loginRequest(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar 
                
                return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'webapp/login.html', {'form': form})


def registracion(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect('inicio')
    else:
        miForm = RegistroForm()
        
        
    return render(request, "webapp/registro.html", {"form":miForm})


# Edicion de perfil

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method  == "POST":
        miForm = editarPerfilForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username = usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect('inicio')
    else:
        miForm = editarPerfilForm(instance=usuario)
    return render ( request, "webapp/editarPerfil.html", {"form":miForm})
            
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "webapp/cambiarClave.html"
    success_url = reverse_lazy('inicio')
    
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username = request.user)
            imagen = miForm.cleaned_data["imagen"]
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            
            avatar = Avatar(user = usuario, imagen = imagen)
            avatar.save()
            
            
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect('inicio')
    else:
        miForm = AvatarForm()
    return render (request, "webapp/agregarAvatar.html", {"form":miForm})


# Opcional

def busquedaWL(request):
    query = request.GET.get('q', '')
    if query:
        results = wishlist.objects.filter(nombre__icontains=query)
    else:
        results = wishlist.objects.none()
    return render(request, 'webapp/busquedaWL.html', {'results': results, 'query': query})
