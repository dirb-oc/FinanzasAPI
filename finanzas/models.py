from django.db import models
from django.contrib.auth.models import User

class Frecuencia(models.Model):
    Tipo = models.CharField(max_length=50, unique=True)

class Ingreso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.descripcion} - {self.cantidad}"

class Gasto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=255)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.descripcion} - {self.cantidad}"
    
class Ahorro(Ingreso):
    nombre = models.CharField(max_length=100)
    fecha_Final = models.DateTimeField()

    def __str__(self):
        return f"{self.nombre} - {self.cantidad}"

class GastoFijo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=255)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    frecuencia = models.ForeignKey(Frecuencia, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.descripcion} - {self.cantidad} ({self.frecuencia})"

class ObjetivosFinancieros(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=255)
    meta = models.DecimalField(max_digits=10, decimal_places=2)
    actual = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.descripcion}"