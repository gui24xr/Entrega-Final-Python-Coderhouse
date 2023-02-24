from app_medicadmin.models import*

def contexto_avisos(request):
    
    lista_de_avisos = aviso_llegada.objects.all()
    

    return {'listado_avisos': lista_de_avisos}