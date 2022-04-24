from django.shortcuts import render
from .models import Usuario

# Create your views here.

def index(request):
    return render (request,'aplicacion1/index.html')

def contacto(request):
    return render (request,'aplicacion1/contacto.html')

def productos(request):
    return render (request,'aplicacion1/productos.html')

def usuarios(request):
    usuario=Usuario.objects.all()
    return render (request,'aplicacion1/usuarios.html',{"data":usuario})

def ejemplo(request):
    return render (request,'aplicacion1/ejemplo.html')
