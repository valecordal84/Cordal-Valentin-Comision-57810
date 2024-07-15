"""
URL configuration for organizadorJuegos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from webapp import views
from django.conf.urls.static import static 
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Inicio
    path('', views.home, name='inicio'),
    path('inicio', views.home, name='inicio'),
    
    #pricipales modelos
    path('wishlist', views.wl, name='wishlist'),
    path('plataformas', views.plataforma, name='plataformas'),
    path('juegosComprar', views.jc, name='juegosComprar'),
    path('juegosTerminados', views.jt, name='juegosTerminados'),
    path('acercaDeMi', views.acercaDeMi, name='acercaDeMi'),
    
    #formularios
    path('wishlistForm', views.wishlistForm, name='wishlistForm'),
    path('plataformasForm', views.plataformasForm, name='plataformasForm'),
    path('jcForm', views.jcForm, name='jcForm'),
    path('jtForm', views.jtForm, name='jtForm'),
    
    #updates
    path('wishlist/update/<str:nombre_wishlist>/', views.wishlistUpdate, name='wishlistUpdate'),
    path('plataformas/update/<str:nombre_plataforma>/', views.plataformasUpdate, name='plataformasUpdate'),
    path('juegosComprar/update/<str:nombre_jc>/', views.jcUpdate, name='jcUpdate'),
    path('juegosTerminados/update/<str:nombre_jt>/', views.jtUpdate, name='jtUpdate'),
    
    #deletes
    path('wishlist/delete/<str:nombre_wishlist>/', views.wishlistDelete, name='wishlistDelete'),
    path('plataformas/delete/<str:nombre_plataforma>/', views.plataformasDelete, name='plataformasDelete'),
    path('juegosComprar/delete/<str:nombre_jc>/', views.jcDelete, name='jcDelete'),
    path('juegosTerminados/delete/<str:nombre_jt>/', views.jtDelete, name='jtDelete'),
    
    #registros
    path('login', views.loginRequest, name='login'),
    path('logout', LogoutView.as_view(template_name="webapp/logout.html"), name='logout'),
    path('registro', views.registracion, name='registro'),
    
    # Editar Perfil
    path('editarPerfil', views.editarPerfil, name='editarPerfil'),
    path('1/password/', views.CambiarClave.as_view(template_name="webapp/cambiarClave.html"), name='cambiarClave'),
    path('agregarAvatar', views.agregarAvatar, name="agregarAvatar"),
    
    # Opcional
    path('busquedaWL', views.busquedaWL, name='busquedaWL'),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)