from django.db import models
from django.utils import timezone

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_dni = models.IntegerField()


def __str__(self):
      return f"{self.nombre}, {self.nacimiento}, {self.direccion}, {self.numero_dni}"

