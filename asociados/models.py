from django.db import models

class Asociado(models.Model):
    numero_cuenta = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    pin = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre} ({self.numero_cuenta})"


