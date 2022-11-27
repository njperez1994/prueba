from django.db import models

# Create your models here.
class viaje(models.Model):
    tipo = models.CharField(max_length=200)
    clase = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    desde = models.CharField(max_length=200)
    hasta = models.CharField(max_length=200)
    fechasalida = models.DateField()
    #la fecha de regreso puede ser un campo vacio para un vuelo
    fecharegreso = models.DateField(blank=True,null=True)