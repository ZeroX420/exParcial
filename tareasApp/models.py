from django.db import models

# Create your models here.

class tareas(models.Model):
    nombre = models.CharField(max_length=32, null=True, blank=True)
    descripcion = models.CharField(max_length=32, null=True, blank=True)
    fechaFin = models.CharField(max_length=32, null=True, blank=True)
    estadoTarea = models.CharField(max_length=32, null=True, blank=True)
    responsableTarea = models.CharField(max_length=32, null=True, blank=True)