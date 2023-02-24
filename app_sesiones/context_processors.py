from app_sesiones.models import*

def contexto_chat(request):
   
    
    chat = mensaje_institucional.objects.all()

    return {'chat': chat}