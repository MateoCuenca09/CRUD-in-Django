from tokenize import blank_re
from django.db import models

# Create your models here.


class Suscriptor(models.Model):
    IdSuscriptor = models.AutoField(primary_key= True)
    Nombre = models.CharField(max_length= 50)
    Apellido = models.CharField(max_length= 50)
    NumeroDocumento = models.CharField(max_length=50)
    TipoDocumento = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=100)
    Email = models.EmailField()
    NombreUsuario = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.Nombre, self.IdSuscriptor,self.TipoDocumento,self.NumeroDocumento)

class Suscripcion(models.Model):
    IdAsociacion=models.AutoField(primary_key=True)
    IdSuscriptor=models.ForeignKey(Suscriptor,to_field="IdSuscriptor",on_delete=models.CASCADE)
    FechaAlta=models.DateTimeField()
    FechaFin=models.DateTimeField(blank = True, null = True)
    MotivoFin=models.CharField(blank = True, null = True, max_length=255)
    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.IdAsociacion, self.IdSuscriptor)
