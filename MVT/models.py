from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField('dd/mm/yyyy')
    numero_dni = models.IntegerField()

def __str__(self):
      return f"{self.nombre}, {self.direccion}, {self.fecha_nacimiento}, {self.numero_dni}, {self.id}"

