from django.shortcuts import render 
from django.template import Template
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from app_medicadmin.models import*
from app_medicadmin.forms import *
from app_medicadmin.modulo_valores_generales import modelo_to_pandas, generar_tabla, procesar_lista_verificados
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.





#/------------------------------------------------------------------------------------------------------------------
#/-------------TURNOS------------------------------------------------------------------------------------------
#/------------------------------------------------------------------------------------------------------------------

class nuevo_turno(LoginRequiredMixin, CreateView):

    login_url = reverse_lazy('login')
    
    model = turno
    template_name = 'app_medicadmin/nuevo_turno.html'
    #fields = ["nombre","apellido"]
    form_class = form_nuevo_turno
    success_url = reverse_lazy('lista_turnos')
    
    
    # Los contextos a las CBV se le pasa sobreescribiendo su metodo get_context_data
    def get_context_data(self,*args, **kwargs):
        context = super(nuevo_turno, self).get_context_data(*args,**kwargs)
        context['titulo_seccion'] = "Nuevo Turno"
        #context['form'] = form_nuevo_paciente()
        return context    
    
    def form_valid(self, form):

        # Aca llamo la funcion que asigna un numero al turno y sera un numero formado x ejemplo con criterios fecha etc, dia juliano, barra
        # Podria enviar un mensaje de creacion correcta, msgbox, etc
        turno.numero_turno = 2
        return super().form_valid(form)
    
    
    
class eliminar_turno(LoginRequiredMixin,DeleteView):

    login_url = reverse_lazy('login')
    
    model = turno
    template_name = 'app_medicadmin/eliminar_turno.html'
    success_url = reverse_lazy('lista_turnos')

    def get_context_data(self,*args, **kwargs):
        context = super(eliminar_turno, self).get_context_data(*args,**kwargs)
        context['titulo_seccion'] = "Eliminar Turno"
        return context    
    

class editar_turno(LoginRequiredMixin,UpdateView):

    login_url = reverse_lazy('login')

    model = turno
    template_name = 'app_medicadmin/editar_paciente.html'
    success_url = reverse_lazy('lista_turnos')#"editar_paciente"
    fields = ['fecha','horario','medico','paciente']

    def get_context_data(self,*args, **kwargs):
        context = super(editar_turno, self).get_context_data(*args,**kwargs)
        context['titulo_seccion'] = "Editar turno"
        return context    
    


class lista_turnos(LoginRequiredMixin,ListView):

    login_url = reverse_lazy('login')
    
    model = turno
    template_name =  'app_medicadmin/listview_turnos.html'
    

    def get_context_data(self,*args, **kwargs):
        context = super(lista_turnos, self).get_context_data(*args,**kwargs)
        context['titulo_seccion'] = "Turnos"
        return context 
    
    
    
    def get(self, request, *args, **kwargs) :
        
        return super().get(request, *args, **kwargs)
    
    

#/------------------------------------------------------------------------------------------------------------------
#/------------- PACIENTES ------------------------------------------------------------------------------------------
#/------------------------------------------------------------------------------------------------------------------
class nuevo_paciente(LoginRequiredMixin,CreateView):

    login_url = reverse_lazy('login')
    
    model = paciente
    template_name = 'app_medicadmin/nuevo_paciente.html'
    fields = ["nombre","apellido","dni"]
    success_url = reverse_lazy('lista_pacientes')
    
    
    def get_context_data(self,*args, **kwargs):
        context = super(nuevo_paciente, self).get_context_data(*args,**kwargs)
        context['titulo_seccion'] = "Nuevo Paciente"
        return context    


class eliminar_paciente(LoginRequiredMixin,DeleteView):

    login_url = reverse_lazy('login')
    
    model = paciente
    template_name = 'app_medicadmin/eliminar_paciente.html'
    success_url = reverse_lazy('lista_pacientes')

    def get_context_data(self,*args, **kwargs):
        context = super(eliminar_paciente, self).get_context_data(*args,**kwargs)
        context['titulo_seccion'] = "Eliminar Paciente"
        return context    
    

class editar_paciente(LoginRequiredMixin,UpdateView):

    login_url = reverse_lazy('login')
    
    model = paciente
    template_name = 'app_medicadmin/editar_paciente.html'
    success_url = reverse_lazy("detalle_paciente/<int:pk>")#"editar_paciente"
    fields = ['nombre','apellido','dni']

    def get_context_data(self,*args, **kwargs):
        context = super(editar_paciente, self).get_context_data(*args,**kwargs)
        context['titulo_seccion'] = "Editar paciente"
        return context    
    

class detalle_paciente(LoginRequiredMixin,DetailView):

    login_url = reverse_lazy('login')
    
    model = paciente
    template_name = 'app_medicadmin/detalle_paciente.html'

    def get_context_data(self,*args, **kwargs):
        context = super(detalle_paciente, self).get_context_data(*args,**kwargs)
        context['titulo_seccion'] = "Detalle Paciente"
        return context    

        
    
class lista_pacientes(LoginRequiredMixin,ListView):

    login_url = reverse_lazy('login')
    
    model = paciente
    template_name =  'app_medicadmin/listview_pacientes.html'
    

    def get_context_data(self,*args, **kwargs):
        context = super(lista_pacientes, self).get_context_data(*args,**kwargs)
        context['titulo_seccion'] = "Pacientes"
        return context 

   
    def get_queryset(self):
        
        # Con la respuesta del servidor vamos a saber que pulso el usuario que quiere buscar
        respuesta_servidor = self.request.GET
        print("Respuesta: ",respuesta_servidor)
        print("Argumentos recibidos: ", self.args)
        
        orden = 'apellido'
        criterio_filtrado = ""
       
        criterio_busqueda = respuesta_servidor.get("CRITERIO_BUSQUEDA")
        buscado = respuesta_servidor.get("MI_BUSQUEDA")
        print("criterio: ", criterio_busqueda, " buscado: ",buscado)

        queryset = paciente.objects.all()
        queryset = paciente.objects.order_by(orden)
    # Si el servidor responde vacio muestra todos los objetos y los ordena por apellido     
        if respuesta_servidor == {}: 
           queryset = paciente.objects.all()
           queryset = paciente.objects.order_by(orden)

        else:
            print("entro")
            if (criterio_busqueda != None) and (buscado != None):
                if criterio_busqueda == 'DNI': queryset = paciente.objects.filter(dni__icontains = buscado)
                elif criterio_busqueda == 'NOMBRE': queryset = paciente.objects.filter(nombre__icontains = buscado)
                elif criterio_busqueda == 'APELLIDO': queryset = paciente.objects.filter(apellido__icontains = buscado)

                print(queryset)
                
           
                
        return queryset
    
    
    
    def get(self, request, *args, **kwargs) :
        
        return super().get(request, *args, **kwargs)
    

#/------------------------------------------------------------------------------------------------------------------
#/------------- MEDICOS-- ------------------------------------------------------------------------------------------
#/------------------------------------------------------------------------------------------------------------------   

class nuevo_medico(LoginRequiredMixin,CreateView):

    login_url = reverse_lazy('login')
    
    model = medico
    template_name = 'app_medicadmin/nuevo_medico.html'
    fields = ["nombre","apellido","dni", "especialidad"]
    success_url = reverse_lazy('lista_medicos')
    
    
    def get_context_data(self,*args, **kwargs):
        context = super(nuevo_medico, self).get_context_data(*args,**kwargs)
        context['titulo_seccion'] = "Nuevo Medico"
        return context    


class eliminar_medico(LoginRequiredMixin,DeleteView):

    login_url = reverse_lazy('login')
    
    model = medico
    template_name = 'app_medicadmin/eliminar_medico.html'
    success_url = reverse_lazy('lista_medicos')

    def get_context_data(self,*args, **kwargs):
        context = super(eliminar_medico, self).get_context_data(*args,**kwargs)
        context['titulo_seccion'] = "Eliminar Medico"
        return context    


class editar_medico(LoginRequiredMixin,UpdateView):

    
    login_url = reverse_lazy('login')
    
    model = medico
    template_name = 'app_medicadmin/editar_medico.html'
    success_url = reverse_lazy("lista_medicos")
    fields = ['nombre','apellido','dni','especialidad']

    def get_context_data(self,*args, **kwargs):
        context = super(editar_medico, self).get_context_data(*args,**kwargs)
        context['titulo_seccion'] = "Editar medico"
        return context    
    

class detalle_medico(LoginRequiredMixin,DetailView):

    login_url = reverse_lazy('login')
    
    
    model = medico
    template_name = 'app_medicadmin/detalle_medico.html'

    def get_context_data(self,*args, **kwargs):
        context = super(detalle_medico, self).get_context_data(*args,**kwargs)
        context['titulo_seccion'] = "Detalle Medico"
        return context    

        

class lista_medicos(LoginRequiredMixin,ListView):

    
    login_url = reverse_lazy('login')
    
    model = medico
    template_name =  'app_medicadmin/listview_medicos.html'
    

    def get_context_data(self,*args, **kwargs):
        context = super(lista_medicos, self).get_context_data(*args,**kwargs)
        context['titulo_seccion'] = "Medicos"
        return context 

   
    def get_queryset(self):
        
        # Con la respuesta del servidor vamos a saber que pulso el usuario que quiere buscar
        respuesta_servidor = self.request.GET
        print("Respuesta: ",respuesta_servidor)
        print("Argumentos recibidos: ", self.args)
        
        orden = 'apellido'
        criterio_filtrado = ""
       
        criterio_busqueda = respuesta_servidor.get("CRITERIO_BUSQUEDA")
        buscado = respuesta_servidor.get("MI_BUSQUEDA")
        print("criterio: ", criterio_busqueda, " buscado: ",buscado)

        queryset = medico.objects.all()
        queryset = medico.objects.order_by(orden)
    # Si el servidor responde vacio muestra todos los objetos y los ordena por apellido     
        if respuesta_servidor == {}: 
           queryset = medico.objects.all()
           queryset = medico.objects.order_by(orden)

        else:
            if (criterio_busqueda != None) and (buscado != None):
                if criterio_busqueda == 'DNI': queryset = medico.objects.filter(dni__icontains = buscado)
                elif criterio_busqueda == 'NOMBRE': queryset = medico.objects.filter(nombre__icontains = buscado)
                elif criterio_busqueda == 'APELLIDO': queryset = medico.objects.filter(apellido__icontains = buscado)
                elif criterio_busqueda == 'ESPECIALIDAD': queryset = medico.objects.filter(especialidad__icontains = buscado)
                
           
                
        return queryset
    
    
    
    def get(self, request, *args, **kwargs) :
        
        return super().get(request, *args, **kwargs)
    
#/------------------------------------------------------------------------------------------------------------------
#/-------------OBRA SOCIAL------------------------------------------------------------------------------------------
#/------------------------------------------------------------------------------------------------------------------


class nuevo_tarjeta_obra_social(LoginRequiredMixin,CreateView):

    login_url = reverse_lazy('login')
    
    model = tarjeta_obra_social
    template_name = 'app_medicadmin/nuevo_nuevo_tarjeta_obra_social.html'
    fields = '__all__'
    success_url = reverse_lazy('lista_pacientes')

    def get_initial(self):
        initial = super().get_initial()
        initial['paciente'] = self.kwargs['id_paciente']
        return initial



class editar_tarjeta_obra_social(LoginRequiredMixin,UpdateView):

    
    login_url = reverse_lazy('login')
    
    model = tarjeta_obra_social
    template_name = 'app_medicadmin/editar_obra_social.html'
    success_url = reverse_lazy("lista_pacientes")#"editar_paciente"
    fields = ['obra_social','num_afiliado']

    def get_context_data(self,*args, **kwargs):
        context = super(editar_tarjeta_obra_social, self).get_context_data(*args,**kwargs)
        context['titulo_seccion'] = "Editar Obra Social"
        return context    
    


#/------------------------------------------------------------------------------------------------------------------
#/-------------TARJETA CONTACTO-------------------------------------------------------------------------------------
#/------------------------------------------------------------------------------------------------------------------

class nuevo_tarjeta_contacto(LoginRequiredMixin,CreateView):

    login_url = reverse_lazy('login')
    
    model = tarjeta_contacto
    template_name = 'app_medicadmin/nuevo_nuevo_tarjeta_obra_social.html'
    #fields = '__all__'
    success_url = reverse_lazy('lista_pacientes')

    
    def get_initial(self):
        initial = super().get_initial()
        initial['paciente'] = self.kwargs['id_paciente']
        return initial


    def get_form_class(self):

        print("AAAAAA", self.kwargs)
        if 'id_paciente' in self.kwargs: # Si me pasaron un paciente.
            return form_contacto_paciente
        elif 'id_medico' in self.kwargs: # Si me pasaron un paciente.
            return form_contacto_medico
        


class editar_tarjeta_contacto_paciente(LoginRequiredMixin,UpdateView):

    
    login_url = reverse_lazy('login')
    
    model = tarjeta_contacto
    template_name = 'app_medicadmin/editar_obra_social.html'
    success_url = reverse_lazy("lista_pacientes")
    #fields = '__all__'

    def get_context_data(self,*args, **kwargs):
        context = super(editar_tarjeta_contacto_paciente, self).get_context_data(*args,**kwargs)
        context['titulo_seccion'] = "Editar datos de contacto paciente"
        return context 

    def get_form_class(self):

        return form_contacto_paciente
    



#/------------------------------------------------------------------------------------------------------------------
#/----------AVISO LLEGADA-------------------------------------------------------------------------------------------
#/------------------------------------------------------------------------------------------------------------------

class nuevo_aviso_llegada(LoginRequiredMixin, CreateView):

    login_url = reverse_lazy('login')
    
    model = aviso_llegada
    template_name = 'app_medicadmin/nuevo_aviso_llegada.html'
    fields = ["paciente"]
    #form_class = form_nuevo_turno
    success_url = reverse_lazy('aviso_llegada_ok') # modificar
    
    
    # Los contextos a las CBV se le pasa sobreescribiendo su metodo get_context_data
    def get_context_data(self,*args, **kwargs):
        context = super(nuevo_aviso_llegada, self).get_context_data(*args,**kwargs)
        context['titulo_seccion'] = "Emitir aviso llegada paciente"
        context['lista'] = aviso_llegada.objects.all()
        #context['form'] = form_nuevo_paciente()
        return context    
    

def aviso_exito(request):

    contexto = {'titulo_seccion':"Mensaje Enviado"}
    return render(request,'app_sesiones/mensaje_enviado.html',contexto)
    

    


#/------------------------------------------------------------------------------------------------------------------
#/----------NOVEDADES-----------------------------------------------------------------------------------------------
#/------------------------------------------------------------------------------------------------------------------

@login_required
def escribir_novedad(request):

  if request.method == 'POST':
      
       contexto = { 'titulo':"Novedades"}
  return render(request,'app_medicadmin/nuevo_aviso_llegada.html' ,contexto)



def novedad_principales(request):


    novedades = post_novedad.objects.all()



    contexto = { 'titulo_seccion':"Novedades",
                  'posts': novedades }


    return render(request,'app_medicadmin/novedades_principal.html' ,contexto)


def a_cerca_de_mi(request):

    return render(request,'app_sesiones/acerca.html')


