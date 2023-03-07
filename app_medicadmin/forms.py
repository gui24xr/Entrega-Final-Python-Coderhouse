from django import forms
from app_medicadmin.models import*
from app_medicadmin.modulo_valores_generales import lista_especialidades



class form_nuevo_turno(forms.ModelForm):
    

    model = turno
    
    class Meta:
        model = turno
        #fields = "__all__"

        fields = ['fecha',
                  'horario',
                  'paciente',
                  'medico']
     
        
 




class form_contacto_paciente(forms.ModelForm):

   
    class Meta:
        
        model = tarjeta_contacto
        
        fields = ['paciente','domicilio_calle','domicilio_numero','domicilio_piso','domicilio_depto','localidad','provincia',
                  'numero_telefonico_1','numero_telefonico_2','email']
        
        labels = {'domicilio_calle':"Calle",'domicilio_numero':"Numero",'domicilio_piso':"Piso",'domicilio_depto':"Depto",
                  'numero_telefonico_1':"Telefono 1",'numero_telefonico_2':"Telefono 2",'email':"E mail"}


class form_contacto_medico(forms.ModelForm):

   
    class Meta:
        
        fields = ['medico','domicilio_calle','domicilio_numero','domicilio_piso','domicilio_depto', 'localidad','provincia',
                  'numero_telefonico_1','numero_telefonico_2','email']
        
        labels = {'domicilio_calle':"Calle",'domicilio_numero':"Numero",'domicilio_piso':"Piso",'domicilio_depto':"Depto",
                  'numero_telefonico_1':"Telefono 1",'numero_telefonico_2':"Telefono 2",'email':"E mail"}



class form_novedad(forms.ModelForm):

    
    
    class Meta:

        model = post_novedad

        fields = ['titulo','contenido','imagen']
        

      
        







 
