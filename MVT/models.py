from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_dni = models.IntegerField()
    nacimiento = models.DateField()


def __str__(self):
      return f"{self.nombre}, {self.direccion}, {self.numero_dni}, {self.nacimiento}"

