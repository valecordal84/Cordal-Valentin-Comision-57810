from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class wishlist(models.Model):
    nombre=models.CharField(max_length=255)
    plataforma=models.CharField(max_length=255)
    genero=models.CharField(max_length=255)
    multijugador=models.BooleanField(default=False)
    solitario=models.BooleanField(default=False)
    
    class Meta:
        ordering= ["nombre"]
        verbose_name="wishlist"
        verbose_name_plural="wishlist"
    
    def __str__(self):
        return self.nombre

class plataformas(models.Model):
    nombrePlataforma=models.CharField(max_length=255)
    membresia=models.BooleanField(default=False)
    
    class Meta:
        ordering= ["nombrePlataforma"]
        verbose_name="plataforma"
        verbose_name_plural="plataformas"
    
    def __str__(self):
        return self.nombrePlataforma
    
        
class juegosComprar(models.Model):
    nombre=models.CharField(max_length=255)
    plataforma=models.CharField(max_length=255)
    precio=models.IntegerField()
    multijugador=models.BooleanField(default=False)
    solitario=models.BooleanField(default=False)
    
    class Meta:
        ordering= ["nombre"]
        verbose_name="juego comprar"
        verbose_name_plural="juegos comprar"
    
    def __str__(self):
        return self.nombre
    

class juegosTerminados(models.Model):
    nombre=models.CharField(max_length=255)
    plataforma=models.CharField(max_length=255)
    genero=models.CharField(max_length=255)
    recomiendo=models.BooleanField(default=False)
    
    class Meta:
        ordering= ["nombre"]
        verbose_name="juego terminado"
        verbose_name_plural="juegos terminados"
    
    def __str__(self):
        return self.nombre
    
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} {self.imagen}"