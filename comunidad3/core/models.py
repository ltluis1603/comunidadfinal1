from django.db import models

# Create your models here.

class Clasificado(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción", null=True, blank=True)
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link = models.URLField(verbose_name="Dirección Web", null=True, blank=True)
    telefono = models.CharField(max_length=200, verbose_name="Telefono", null=True, blank=True)
    whatsapp = models.CharField(max_length=200, verbose_name="Whatsapp", null=True, blank=True) 
    email = models.EmailField(max_length=200, verbose_name="Email", null=True, blank=True)
    facebook = models.CharField(max_length=200, verbose_name="Facebook", null=True, blank=True)
    twitter =  models.CharField(max_length=200, verbose_name="Twitter", null=True, blank=True)
    instagram =  models.CharField(max_length=200, verbose_name="Instagram", null=True, blank=True) 
    youtube =  models.CharField(max_length=200, verbose_name="Youtube", null=True, blank=True)  
    mercado = models.CharField(max_length=200, verbose_name="Mercado Libre", null=True, blank=True) 
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ["created"]

    def __str__(self):
        return self.title