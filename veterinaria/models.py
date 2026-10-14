from django.db import models

# Create your models here.
from django.db import models
 
class Cliente(models.Model):
    nombre = models.CharField(max_length=60)
    rut = models.CharField(max_length=9, unique=True)
    telefono = models.CharField(max_length=9, unique=True)
    monto = models.DecimalField()
    orden = models.PositiveSmallIntegerField(default=1)

 
    class Meta:
        ordering = ['orden']
 
    def __str__(self):
        return self.nombre
 
class Atencion(models.Model):
    nombre = models.CharField(max_length=120)
    raza = models.CharField(max_length=100)
    edad = models.PositiveSmallIntegerField()
    dueño = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='Atencions',
    )