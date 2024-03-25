from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Armaduras(models.Model):

    nombre_armadura = models.CharField(max_length=30)
    tipo_armadura = models.CharField(max_length=30)
    lv_armadura = models.IntegerField(default= 1)

    def __str__(self):
        return f"{self.nombre_armadura}---{self.tipo_armadura}---{self.lv_armadura}"

class Personajes (models.Model):
    nombre = models.CharField(max_length = 60)
    raza = models.CharField(max_length = 60)
    averno = models.IntegerField(default= 1)

    def __str__(self):
        return f"{self.nombre}---{self.raza}---{self.averno}"

class Build(models.Model):
    nombre = models.CharField(max_length = 60)
    tipo_daño = models.CharField(max_length = 60)
    Total_daño = models.IntegerField(default= 100)


    def __str__(self):
        return f"{self.nombre}---{self.tipo_daño}---{self.Total_daño}"


class Pet (models.Model):
    nombre = models.CharField(max_length = 60)
    raza = models.CharField(max_length = 60)
    nivel = models.IntegerField(default= 1)

    def __str__(self):
        return f"{self.nombre}---{self.raza}---{self.nivel}"
    

class Avatar(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)