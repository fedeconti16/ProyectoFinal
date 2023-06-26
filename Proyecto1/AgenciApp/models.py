from django.db import models

# Create your models here.

class clientesCompradores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    celular = models.IntegerField()
    autoComprado = models.CharField(max_length=40)
    montoOperacionComp = models.IntegerField()

class clientesVendedores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    celular = models.IntegerField()
    autoVendido = models.CharField(max_length=40)
    montoOperacionVent = models.IntegerField()

class autosEnStock(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    km = models.IntegerField()
    precio = models.IntegerField()


class empleadosVendedores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    celular = models.IntegerField()
    operacionesConcretadas = models.IntegerField()
    montoVendido = models.IntegerField()