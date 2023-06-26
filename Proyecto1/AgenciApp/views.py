from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from AgenciApp.models import *
#from AppCoder.forms import formSetEstudiante


def inicio(request):
    return render(request, "AgenciApp/inicio.html")

def autosEnStock(request):
    return render(request, "AgenciApp/autosEnStock.html")

def clientesCompradores(request):
    return render(request, "AgenciApp/clientesCompradores.html")

def clientesVendedores(request):
    return render(request, "AgenciApp/clientesVendedores.html")

def empleadosVendedores(request):
    return render(request, "AgenciApp/empleadosVendedores.html")

#def setEstudiantes(request):
#    if request.method == 'POST':
#        miFormulario = formSetEstudiante(request.POST)
#        print(miFormulario)
#        if miFormulario.is_valid:
#            data = miFormulario.cleaned_data
#            estudiante = Estudiante(nombre=data["nombre"],apellido=data["apellido"], email=data["email"])    
#            estudiante.save()
#            return render(request,"AppCoder/inicio.html")    
#    else:
#        miFormulario = formSetEstudiante()
#    return render(request, "AppCoder/setEstudiantes.html", {"miFormulario":miFormulario})
#
#    """if request.method == 'POST':
#        estudiante = Estudiante(nombre=request.POST["nombre"],apellido=request.POST["apellido"], email=request.POST["email"])
#        estudiante.save()
#        return render(request,"AppCoder/inicio.html")
#    return render(request, "AppCoder/setEstudiantes.html")"""
#
#def getEstudiantes(request):
#    return render(request, "AppCoder/getEstudiantes.html")
#
#def buscarEstudiante(request):
#    if request.GET["nombre"]:
#        nombre = request.GET["nombre"]
#        estudiantes = Estudiante.objects.filter(nombre = nombre)
#        return render(request, "AppCoder/getEstudiantes.html", {"estudiantes":estudiantes})
#    else:
#        respuesta = "No se enviaron datos"
#    
#    return HttpResponse(respuesta)