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
#/---------- APP_ SESIONES --------------------------------------------------------//

from django.contrib import admin
from django.urls import path
from app_sesiones.views import*
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('principal/', pagina_principal,name = 'principal'),
    path('acerca', a_cerca_de_mi ,name = 'a_cerca'),
    path('login2/', inicio_sesion.as_view(),name = 'login2'),
    path('login/', iniciar_sesion ,name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'app_sesiones/logout.html'), name = 'cerrar_sesion'),
    path('registro/', registro_usuario ,name = 'registro_usuario'),
    path('edicion_seguridad/', editar_seguridad ,name = 'edicion_seguridad'),
    path('edicion_perfil/<int:pk>', editar_perfil.as_view() ,name = 'edicion_perfil'),
    path('sitio_en_construccion', sitio_en_construccion ,name = 'sitio_en_construccion'),
    path('about', about ,name = 'about'),
    #path('mensaje_institucional', nuevo_mensaje_institucional.as_view() ,name = 'mensaje_institucional'),
    path('sms', nuevo_sms ,name = 'nuevo_sms'),
    
    
    ]




    
    
   