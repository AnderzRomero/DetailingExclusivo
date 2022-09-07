from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    telefono = models.IntegerField()
    email = models.EmailField(unique=True)

class TrabajoRealizar(models.Model):
    trabajo_a_realizar = models.CharField(max_length=40)
    fecha_de_ingreso = models.DateField()

class Automovil(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    modelo = models.IntegerField()
    color = models.CharField(max_length=10)

class Empleado(models.Model):
   nombre = models.CharField(max_length=30)
   apellido = models.CharField(max_length=30)
   cargo = models.CharField(max_length=30)
   email = models.EmailField(unique=True)