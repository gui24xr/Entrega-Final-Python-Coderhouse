from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


    
class perfil_usuario(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=10)
    foto_perfil = models.ImageField(upload_to='avatares',null= True,blank=True)
    categoria = models.CharField( max_length=10, choices = [("MEDICO", "MEDICO"), ("SECRETARIA", "SECRETARIA"),("ADMIN", "ADMIN")], null=True)

    def __str__(self):
        return f"{self.user} - {self.foto_perfil}"
    


class mensaje_institucional(models.Model):

    autor =  models.CharField(max_length=30)
    #fecha = models.DateField(verbose_name="Fecha Anunciado")
    #horario = models.TimeField(verbose_name="Horario Anunciado")
    mensaje = models.TextField()
    


