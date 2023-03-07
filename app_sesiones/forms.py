
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms 

from django.contrib.auth.models import User
from app_sesiones.models import perfil_usuario


class UserRegisterForm(UserCreationForm):
    
    nombre = forms.CharField()
    apellido = forms.CharField() 
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

  
 
    class Meta:
        
        model = User
        
        fields = ['username',
                   'email', 
                   'password1', 
                   'password2']
        
        labels = {'username': 'Usuario',
                   'email':   'Email', 
                   }
        
        
        
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}



class form_inicio_sesion(AuthenticationForm):

     
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    


class UserEditForm(UserCreationForm):
    
    #nombre = forms.CharField()
    #apellido = forms.CharField()
    #email = forms.EmailField(label='Modificar Email')
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        #fields = ('nombre','apellido','email', 'password1', 'password2')
        fields = ['password1', 'password2']



class form_edicion_perfil(forms.ModelForm):

    #foto_perfil = forms.ImageField(widget = forms.FileInput())
    #foto_perfil = forms.ImageField(widget=forms.ImageField)
    class Meta:
        model = perfil_usuario
        fields = ['apellido','nombre','dni','categoria','foto_perfil']
        labels = {'apellido: aaaaaaaaaaaaaaaaaaaaaaaaaaa'}
        widgets = { 'foto_perfil':forms.FileInput() }

