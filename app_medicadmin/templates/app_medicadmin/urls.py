"""administracion_consultorios_medicos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_medicadmin.views import*

urlpatterns = [
     
    # CRUD PACIENTES
    path('nuevo_paciente/', nuevo_paciente.as_view(),name="nuevo_paciente"),
    path('lista_pacientes', lista_pacientes.as_view(),name="lista_pacientes"),
    path('detalle_paciente/<int:pk>', detalle_paciente.as_view(),name="detalle_paciente"),
    path('editar_paciente/<int:pk>', editar_paciente.as_view(),name="editar_paciente"),
    path('eliminar_paciente/<int:pk>', eliminar_paciente.as_view(),name="eliminar_paciente"),
    
    
    # CRUD MEDICOS
    path('nuevo_medico/', nuevo_medico.as_view(),name="nuevo_medico"),
    path('lista_medicos/', lista_medicos.as_view(),name="lista_medicos"),
    path('detalle_medico/<int:pk>', detalle_medico.as_view(),name="detalle_medico"),
    path('editar_medico/<int:pk>', editar_medico.as_view(),name="editar_medico"),
    path('eliminar_medico/<int:pk>', eliminar_medico.as_view(),name="eliminar_medico"),
    
    
    # CRUD TARJETA DE CONTACTOS 
    path('nueva_tarjeta_contacto/<int:id_paciente>', nuevo_tarjeta_contacto.as_view(),name="nuevo_contacto"),
    path('nueva_tarjeta_contactowwwwwww/<int:id_medico>', nuevo_tarjeta_contacto.as_view(),name="nuevo_contacto_medico"),
    path('editar_tarjeta_contacto/<int:pk>', editar_tarjeta_contacto_paciente.as_view(),name="editar_tarjeta_contacto_paciente"),
    
    
    # CRUD TARJETAS DE OBRA SOCIAL
    path('nueva_credencial_os/<int:id_paciente>', nuevo_tarjeta_obra_social.as_view(),name="nuevo_tarjeta_obra_social"),
    path('editar_obra_social/<int:pk>', editar_tarjeta_obra_social.as_view(),name="editar_obra_social"),

    # CRUD TURNOS
    path('nuevo_turno/', nuevo_turno.as_view(),name="nuevo_turno"),
    path('lista_turnos', lista_turnos.as_view(),name="lista_turnos"),
    path('editar_turno/<int:pk>', editar_turno.as_view(),name="editar_turno"),
    path('eliminar_turno/<int:pk>', eliminar_turno.as_view(),name="eliminar_turno"),
    


     # AVISOS DE LLEGADA
    path('nuevo_aviso_llegada/', nuevo_aviso_llegada.as_view(),name="nuevo_aviso_llegada"),
    path('aviso_exitoso/', aviso_exito,name="aviso_llegada_ok"),

    
    # NOVEDADES
   path('novedades/', novedad_principales,name="novedades_principal"),



]
