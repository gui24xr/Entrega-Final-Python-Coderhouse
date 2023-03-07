from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
#from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from app_sesiones.forms import UserRegisterForm,form_inicio_sesion, UserEditForm, form_edicion_perfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import UpdateView
from app_sesiones.models import*
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from datetime import datetime


# Create your views here.

@login_required
def pagina_principal(request):





    
    return render(request,'app_sesiones/principal.html')


# Esto sucede cuando inicio sesion. 
# al pedo este class    
class inicio_sesion(LoginView):

    redirect_authenticated_user = False
    template_name = 'app_sesiones/login2.html'

    def get_success_url(self) -> str:
        
        return reverse_lazy('nuevo_paciente')
    
    def form_invalid(self, form):
        
        print(self.request)
        messages.error(self.request,'Usuario y/o contraseña erroneos.')
        return self.render_to_response(self.get_context_data(form=form))
    
    def get(self, request, *args, **kwargs):


        print("AAAAABBBVV:", self.request.POST)
        return super().get(request, *args, **kwargs)


    
    
def iniciar_sesion2(request):

    respuesta_servidor = request
    print("Respuesta: ", respuesta_servidor)


    if request.method == "POST":
                        # data es un parametro que se le pasa para que guarde ahi el resultado de post
        formulario = AuthenticationForm(request, data = request.POST)

        if formulario.is_valid():
            
            usuario = formulario.cleaned_data.get("username")
            clave = formulario.cleaned_data.get("password")

            user = authenticate(username= usuario, password = clave) 
            #print("Devolucion authenticate: ", user)

            if user is not None:

                login(request, user)
                #print("Login Devolvio: ",devolucion_login)
            
                entorno = {'mensaje':" SESION INICIADA"}
                
                return render(request,'app_sesiones/hijo.html',entorno)
        
            else: 
                entorno = {'mensaje':"INCORRECTO"}
                return render(request,'app_sesiones/hijo.html',entorno)
        else:
            entorno = {'mensaje':"ELSE ERRONEO"}
            return render(request,'app_sesiones/hijo.html',entorno)



    formulario_inicio_sesion = AuthenticationForm()

    entorno = { 'form': formulario_inicio_sesion}
    return render(request,'app_sesiones/login.html', entorno)




def iniciar_sesion(request):

    respuesta_servidor = request
    print("Respuesta: ", respuesta_servidor)


    if request.method == "POST":
                        # data es un parametro que se le pasa para que guarde ahi el resultado de post
        formulario = form_inicio_sesion(request, data = request.POST)

        if formulario.is_valid():
            
            usuario = formulario.cleaned_data.get("username")
            clave = formulario.cleaned_data.get("password")

            user = authenticate(username= usuario, password = clave) 
            #print("Devolucion authenticate: ", user)

            if user is not None:

                login(request, user)
                #print("Login Devolvio: ",devolucion_login)
            
                entorno = {'titulo_seccion':" BIENVENIDA",
                           'saludo':"Bienvenido"}
                
                return render(request,'app_sesiones/bienvenida_usuario.html',entorno)
        
            else: 
                entorno = {'mensaje':"INCORRECTO"}
                return render(request,'app_sesiones/hijo.html',entorno)
        else:
            entorno = {'mensaje':"ELSE ERRONEO", 'form': formulario}
            return render(request,'app_sesiones/login.html',entorno)



    formulario_inicio_sesion = form_inicio_sesion()

    entorno = { 'form': formulario_inicio_sesion}
    return render(request,'app_sesiones/login.html', entorno)





def registro_usuario(request):


    if request.method == "POST":
          
        formulario_registro = UserRegisterForm(request.POST)

        if formulario_registro.is_valid():
              
            username = formulario_registro.cleaned_data.get('username')
            formulario_registro.save()
              
            # Yo lo que busco ahora es crear una instancia de perfil y ligarla a este usuario.
            
            usuario_creado = User.objects.get(username__iexact=username) # Agarro la instancia recien creada.
            nuevo_perfil_usuario  = perfil_usuario() # Creo un perfil
            nuevo_perfil_usuario.user = usuario_creado # Le asigno la nueva instancia en su relacion one to one
            nuevo_perfil_usuario.nombre = formulario_registro.cleaned_data.get('nombre')
            nuevo_perfil_usuario.apellido = formulario_registro.cleaned_data.get('apellido')
            
            nuevo_perfil_usuario.foto_perfil = "avatares/avatdefault.jpg"
            nuevo_perfil_usuario.save() # Guardo y ya tengo ligado el nuevo usuario con su instancia de perfil asignada.
            
            entorno = {'mensaje': " USUARIO CREADO "}
            return render(request,'app_sesiones/usuario_registrado.html',entorno)
    

    else:
        formulario_registro = UserRegisterForm()  


    entorno = { 'form': formulario_registro}
    return render(request,'app_sesiones/registro_usuario.html',entorno)



@login_required
def editar_seguridad (request):

    usuario = request.user
  

    if request.method == 'POST':
        
        mi_formulario = UserEditForm(request.POST)

        if mi_formulario.is_valid():
            
            informacion_ingresada = mi_formulario.cleaned_data

            usuario.password1 = informacion_ingresada['password1']
            usuario.password2 = informacion_ingresada['password2']
            usuario.save()

            entorno = {'mensaje':"La contraseña fue editada con exito."}
            return render(request,'app_sesiones/edicion_seguridad.html',entorno)
        
    else:

        mi_formulario = UserEditForm()
        entorno = {'formulario':mi_formulario}

        return render(request,'app_sesiones/edicion_seguridad.html',entorno)


    
    
  

        mi_formulario = UserEditForm(initial={ 'email' : usuario.email})

        entorno = { 'formulario' : mi_formulario}

        return render(request,'app_sesiones/edicion_seguridad.html',entorno)






# FUERA DE SERVICIO 5/3/22
class _anulada_editar_perfil(LoginRequiredMixin,UpdateView):

    login_url = reverse_lazy('login')

    model = perfil_usuario
    template_name = 'app_sesiones/edicion_perfil.html'
    success_url = reverse_lazy('novedades_principal')#"editar_paciente"
    #fields = ['apellido','nombre','dni','categoria','foto_perfil']
    form_class = form_edicion_perfil

    def get_context_data(self,*args, **kwargs):
        context = super(editar_perfil, self).get_context_data(*args,**kwargs)
        #context['titulo_seccion'] = "Editar Perfil"
        return context    
    


def editar_perfil(request):

    # Me paro en la instancia a editar.
    perfil_a_editar = perfil_usuario.objects.get(user = request.user)

    if request.method == 'POST':

        print("FILES: ", request.FILES)
       
        respuesta_servidor = request.POST
        respuesta_servidor_imagen = request.FILES
        #print("Respuesta POST: ", respuesta_servidor)
        #print("Respuesta IMAGEN: ", respuesta_servidor_imagen)
        
        perfil_a_editar.nombre = respuesta_servidor.get('nombre')
        perfil_a_editar.apellido = respuesta_servidor.get('apellido')
        perfil_a_editar.dni = respuesta_servidor.get('dni')
        perfil_a_editar.user.email = respuesta_servidor.get('email')

        
        if respuesta_servidor_imagen != {}:
         perfil_a_editar.foto_perfil = respuesta_servidor_imagen.get('archivo_imagen')

        perfil_a_editar.save()

        return render(request, 'app_sesiones/edicion_perfil.html' )
        
        
    return render(request, 'app_sesiones/edicion_perfil.html' )
    
    
    


   



def sitio_en_construccion(request):

   return render(request, 'app_sesiones/sitio_en_construccion.html')



def about(request):

   return render(request, 'app_sesiones/about.html')


class nuevo_mensaje_institucional(LoginRequiredMixin, CreateView):

    login_url = reverse_lazy('login')
    
    model = mensaje_institucional
    template_name = 'app_sesiones/mensaje_chat.html'
    fields = ["mensaje"]
    #form_class = form_nuevo_turno
    success_url = reverse_lazy('principal') # modificar
    
    
    # Los contextos a las CBV se le pasa sobreescribiendo su metodo get_context_data
    def get_context_data(self,*args, **kwargs):
        context = super(nuevo_mensaje_institucional, self).get_context_data(*args,**kwargs)
        context['titulo_seccion'] = "Mensaje institucional"
        return context    
    
    def form_valid(self, form):


        return super().form_valid(form)
    

@login_required(login_url='login')  
def nuevo_sms(request):

    if request.method == "POST":

        respuesta_servidor = request.POST
        
        print(respuesta_servidor)
        nuevo_mensaje = mensaje_institucional()
        nuevo_mensaje.autor = request.user.perfil_usuario.nombre + " " + request.user.perfil_usuario.apellido
        nuevo_mensaje.mensaje =  respuesta_servidor.get("mensaje_enviado")
        
        nuevo_mensaje.save()

        contexto = {'titulo_seccion':"Mensaje Enviado"}
        return render(request,'app_sesiones/mensaje_enviado.html',contexto)

    
    
    else:

        contexto = {'titulo_seccion':"Mensaje Institucional"}
        return render(request,'app_sesiones/mensaje_chat.html',contexto)
    
 



def a_cerca_de_mi(request):

    perfil_propio = perfil_usuario.objects.filter(dni__iexact = '1111111111')
    print(perfil_propio)
    
    contexto = { 'foto': perfil_propio }
    return render(request,'app_sesiones/acerca.html',contexto)    
   