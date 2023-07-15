from django.db import models

# Create your models here.

    
CONTACTO_MEDIA = [
    ("llamada", "Llamada"),
    ("whatsapp", "Whatsapp"),
    ("correo", "Correo"),
]

class Clientes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    telefono = models.CharField(max_length=100, verbose_name="Telefono")
    correo = models.EmailField(max_length=100, verbose_name="Correo")
    articulo = models.CharField(max_length=200, verbose_name="Articulo")
    especificaciones = models.TextField(null=True, verbose_name="Especificaciones")
    direccion = models.TextField(null=True, verbose_name="Direccion")
    comentarios = models.TextField(null=True, verbose_name="Comentarios")
    contacto = models.CharField(max_length=10, blank=True, choices=CONTACTO_MEDIA, verbose_name="Contacto")
    
    
    def __str__(self):
        fila = self-id + self.nombre
        return fila 
    
    
