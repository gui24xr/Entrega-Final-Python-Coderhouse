from django.db import models
from app_medicadmin.modulo_valores_generales import*
from django.utils import timezone, datetime_safe
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.+
class tarjeta_obra_social(models.Model):
    
    paciente = models.OneToOneField('paciente',null=True,blank=True, on_delete=models.CASCADE)
    obra_social = models.CharField(max_length=24,choices=lista_obras_sociales, default= "S/N") #Poner opciones precargadas y por defecto sin obra social
    num_afiliado = models.CharField(max_length=20,null=True,blank=True)

    
    def __str__(self):
        return f"CARNET: {self.obra_social} "

    
class tarjeta_contacto(models.Model):

    paciente = models.OneToOneField('paciente', null=True,blank=True,on_delete=models.CASCADE)
    medico = models.OneToOneField('medico', null=True,blank=True,on_delete=models.CASCADE)
    localidad = models.CharField(max_length=20,null=True,blank=True)
    provincia = models.CharField(max_length=24,choices=lista_provincias, null=True)
    domicilio_calle = models.CharField(max_length=20)
    domicilio_numero = models.CharField(max_length=5)
    domicilio_piso = models.CharField(max_length=2)
    domicilio_depto = models.CharField(max_length=2)
    numero_telefonico_1 = models.CharField(max_length=14)
    numero_telefonico_2 = models.CharField(max_length=14)
    email = models.EmailField()

    def __str__(self):
        

        if self.paciente != None : cadena = f"Datos de contacto de {self.paciente.apellido} {self.paciente.nombre}."
        if self.medico != None : cadena = f"Datos de contacto de {self.medico.apellido} {self.medico.nombre}."
        
        return cadena




class paciente(models.Model):

    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=24)
    apellido = models.CharField(max_length=24)
    

    def __str__(self):
        return f"Paciente {str.upper(self.apellido)} {self.nombre}"
    
    
    
    


class medico(models.Model):

      
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=24)
    apellido = models.CharField(max_length=24)
    especialidad = models.CharField(max_length=30, choices= lista_especialidades)
   

    def __str__(self):
        return f"Dr/a: {str.upper(self.apellido)} {self.nombre}, {self.especialidad}"
    
  
    
    
class turno(models.Model):

    numero_turno : models.IntegerField(verbose_name= "Turno Numero: ")
    fecha = models.DateField(verbose_name="Fecha Turno",default=datetime.now())
    horario = models.TimeField(verbose_name="Horario Turno",default=datetime.now())
    paciente = models.ForeignKey(paciente, null=True,blank=True,on_delete=models.CASCADE)
    medico = models.ForeignKey(medico,null=True,blank=True,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"TURNO: {self.fecha} {self.horario}, {self.paciente}, {self.medico}"
    


#Avisos de llegada generados por secretaria a medicos de llegada de pacientes.
class aviso_llegada(models.Model):

    paciente = models.ForeignKey(paciente, null=True,blank=True,on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha Anunciado",auto_now_add=True)
    horario = models.TimeField(verbose_name="Horario Anunciado", auto_now_add=True)



class post_novedad(models.Model):
    

    titulo = models.CharField(max_length=200, 
        verbose_name="Título")
    contenido = models.TextField(
        verbose_name="Contenido")
    imagen = models.ImageField(verbose_name="Imagen", 
        upload_to="imagenes", blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, 
        verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, 
        verbose_name="Fecha de edición")
    autor = models.ForeignKey(User, null=True,blank=True,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Novedad"
        verbose_name_plural = "Novedades"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo