from django.db import models

# Create your models here.
class Platos(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=4,decimal_places=2)