from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from AgenciApp.models import *
from AgenciApp.forms import *
from django.shortcuts import redirect


def inicio(request):
    return render(request, "AgenciApp/inicio.html")

#def AutosEnStock(request):
#    Autos = autosEnStock.objects.all()
#    return render(request, "AgenciApp/autosEnStock.html",{"Autos": Autos})

def setAutosEnStock(request):
    Autos = autosEnStock.objects.all()
    if request.method == 'POST':
        auto = autosEnStock(marca=request.POST["marca"],modelo=request.POST["modelo"],km=request.POST["km"],precio=request.POST["precio"])
        auto.save()  
        miFormulario = autosFormulario()
        return render(request, "AgenciApp/setAutosEnStock.html", {"miFormulario":miFormulario, "Autos":Autos})
    else:
        miFormulario = autosFormulario()
    return render(request, "AgenciApp/setAutosEnStock.html", {"miFormulario":miFormulario, "Autos":Autos})

def eliminarAuto(request, marca_auto, modelo_auto):
    auto = autosEnStock.objects.get(marca = marca_auto, modelo = modelo_auto)
    auto.delete()
    miFormulario = autosFormulario()
    Autos = autosEnStock.objects.all()
    return redirect('setAutosEnStock')
#    return render(request, "AgenciApp/setAutosEnStock.html", {"miFormulario":miFormulario, "Autos":Autos})


#def ClientesCompradores(request):
#    return render(request, "AgenciApp/clientesCompradores.html")

#def ClientesVendedores(request):
#    return render(request, "AgenciApp/clientesVendedores.html")

#def EmpleadosVendedores(request):
#    return render(request, "AgenciApp/empleadosVendedores.html")

#def AutosEnStock(request):
#    if request.method == 'POST':
#        miFormulario = autosFormulario(request.POST)
#        print(miFormulario)
#        if miFormulario.is_valid():
#            data = miFormulario.cleaned_data
#            auto = autosEnStock(marca=data["marca"],modelo=data["modelo"],km=data["km"],precio=data["precio"])    
#            auto.save()
#            return render(request,"AgenciApp/inicio.html")    
#    else:
#        miFormulario = autosFormulario()
#    return render(request, "AgenciApp/setAutosEnStock.html", {"miFormulario":miFormulario})



def ClientesCompradores(request):
    if request.method == 'POST':
        miFormulario = clientesFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            cliente = clientesCompradores(nombre=data["nombre"],apellido=data["apellido"],email=data["email"],celular=data["celular"],autoComprado=data["autoComprado"],montoOperacionComp=data["montoOperacionComp"])    
            cliente.save()
            return render(request,"AgenciApp/inicio.html")    
    else:
        miFormulario = clientesFormulario()
    return render(request, "AgenciApp/setClientesCompradores.html", {"miFormulario":miFormulario})

def ClientesVendedores(request):
    if request.method == 'POST':
        miFormulario = clientesVendFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            cliente = clientesVendedores(nombre=data["nombre"],apellido=data["apellido"],email=data["email"],celular=data["celular"],autoVendido=data["autoVendido"],montoOperacionVent=data["montoOperacionVent"])    
            cliente.save()
            return render(request,"AgenciApp/inicio.html")    
    else:
        miFormulario = clientesVendFormulario()
    return render(request, "AgenciApp/setClientesVendedores.html", {"miFormulario":miFormulario})

def EmpleadosVendedores(request):
    if request.method == 'POST':
        miFormulario = empleadosFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            empleado = empleadosVendedores(nombre=data["nombre"],apellido=data["apellido"],email=data["email"],celular=data["celular"],operacionesConcretadas=data["operacionesConcretadas"],montoVendido=data["montoVendido"])    
            empleado.save()
            return render(request,"AgenciApp/inicio.html")    
    else:
        miFormulario = empleadosFormulario()
    return render(request, "AgenciApp/setEmpleadosVendedores.html", {"miFormulario":miFormulario})

def getAutosEnStock(request):
    return render(request, "AgenciApp/getAutosEnStock.html")

def buscarAutosEnStock(request):
    marca = request.GET.get("marca")
    if marca:
        autos = autosEnStock.objects.filter(marca=marca)
        return render(request, "AgenciApp/getAutosEnStock.html", {"autos": autos, "marca": marca})
    else:
        respuesta = "No se enviaron datos"
    
    return HttpResponse(respuesta)