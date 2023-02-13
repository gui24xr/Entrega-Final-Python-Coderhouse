from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def vista_login(request):

    return render(request,'app_medicadmin/login.html')

def vista_prueba_plantilla_padre(request):

    return render(request,'app_medicadmin/padre2.html')