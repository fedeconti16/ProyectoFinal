from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from AgenciApp.models import *
from AgenciApp.forms import *
from django.shortcuts import redirect


def inicio(request):
    return render(request, "AgenciApp/inicio.html")

############################################################################################################

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

def editarAuto(request, marca_auto, modelo_auto):
    auto = autosEnStock.objects.get(marca=marca_auto, modelo=modelo_auto)
    if request.method == 'POST':
        miFormulario = autosFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            auto.marca = data['marca']
            auto.modelo = data['modelo']
            auto.km = data['km']
            auto.precio = data['precio']
            auto.save()

            miFormulario = autosFormulario()
            Autos = autosEnStock.objects.all()
            return redirect('setAutosEnStock')
    else:
        miFormulario = autosFormulario(initial={'marca': auto.marca, 'modelo': auto.modelo, 'km': auto.km, 'precio': auto.precio})

    return render(request, "AgenciApp/editarAutosEnStock.html", {"miFormulario": miFormulario})

#########################################################################################################################

def setClientesCompradores(request):
    Clientes = clientesCompradores.objects.all()
    if request.method == 'POST':
        cliente = clientesCompradores(nombre=request.POST["nombre"],apellido=request.POST["apellido"],email=request.POST["email"],celular=request.POST["celular"], autoComprado=request.POST["autoComprado"], montoOperacionComp=request.POST["montoOperacionComp"])
        cliente.save()  
        miFormulario = clientesFormulario()
        return render(request, "AgenciApp/setClientesCompradores.html", {"miFormulario":miFormulario, "Clientes":Clientes})
    else:
        miFormulario = clientesFormulario()
    return render(request, "AgenciApp/setClientesCompradores.html", {"miFormulario":miFormulario, "Clientes":Clientes})

def eliminarClienteComprador(request, email_cliente):
    cliente = clientesCompradores.objects.get(email = email_cliente)
    cliente.delete()
    miFormulario = clientesFormulario()
    Clientes = clientesCompradores.objects.all()
    return redirect('setClientesCompradores')

def editarClienteComprador(request, email_cliente):
    cliente = clientesCompradores.objects.get(email = email_cliente)
    if request.method == 'POST':
        miFormulario = clientesFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            cliente.nombre = data['nombre']
            cliente.apellido = data['apellido']
            cliente.email = data['email']
            cliente.celular = data['celular']
            cliente.autoComprado = data['autoComprado']
            cliente.montoOperacionComp = data['montoOperacionComp']
            cliente.save()

            miFormulario = clientesFormulario()
            Clientes = clientesCompradores.objects.all()
            return redirect('setClientesCompradores')
    else:
        miFormulario = clientesFormulario(initial={'nombre': cliente.nombre, 'apellido': cliente.apellido, 'email': cliente.email, 'celular': cliente.celular, 'autoComprado': cliente.autoComprado, 'montoOperacionComp': cliente.montoOperacionComp})

    return render(request, "AgenciApp/editarClientesCompradores.html", {"miFormulario": miFormulario})


#########################################################################################################################

def setClientesVendedores(request):
    Clientes = clientesVendedores.objects.all()
    if request.method == 'POST':
        cliente = clientesVendedores(nombre=request.POST["nombre"],apellido=request.POST["apellido"],email=request.POST["email"],celular=request.POST["celular"], autoVendido=request.POST["autoVendido"], montoOperacionVent=request.POST["montoOperacionVent"])
        cliente.save()  
        miFormulario = clientesVendFormulario()
        return render(request, "AgenciApp/setClientesVendedores.html", {"miFormulario":miFormulario, "Clientes":Clientes})
    else:
        miFormulario = clientesVendFormulario()
    return render(request, "AgenciApp/setClientesVendedores.html", {"miFormulario":miFormulario, "Clientes":Clientes})

def eliminarClienteVendedor(request, email_cliente):
    cliente = clientesVendedores.objects.get(email = email_cliente)
    cliente.delete()
    miFormulario = clientesVendFormulario()
    Clientes = clientesVendedores.objects.all()
    return redirect('setClientesVendedores')

def editarClienteVendedor(request, email_cliente):
    cliente = clientesVendedores.objects.get(email = email_cliente)
    if request.method == 'POST':
        miFormulario = clientesVendFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            cliente.nombre = data['nombre']
            cliente.apellido = data['apellido']
            cliente.email = data['email']
            cliente.celular = data['celular']
            cliente.autoVendido = data['autoVendido']
            cliente.montoOperacionVent = data['montoOperacionVent']
            cliente.save()

            miFormulario = clientesVendFormulario()
            Clientes = clientesVendedores.objects.all()
            return redirect('setClientesVendedores')
    else:
        miFormulario = clientesVendFormulario(initial={'nombre': cliente.nombre, 'apellido': cliente.apellido, 'email': cliente.email, 'celular': cliente.celular, 'autoVendido': cliente.autoVendido, 'montoOperacionVent': cliente.montoOperacionVent})

    return render(request, "AgenciApp/editarClientesVendedores.html", {"miFormulario": miFormulario})

#########################################################################################################################

def setEmpleadosVendedores(request):
    Empleados = empleadosVendedores.objects.all()
    if request.method == 'POST':
        empleado = empleadosVendedores(nombre=request.POST["nombre"],apellido=request.POST["apellido"],email=request.POST["email"],celular=request.POST["celular"], operacionesConcretadas=request.POST["operacionesConcretadas"], montoVendido=request.POST["montoVendido"])
        empleado.save()  
        miFormulario = empleadosFormulario()
        return render(request, "AgenciApp/setEmpleadosVendedores.html", {"miFormulario":miFormulario, "Empleados":Empleados})
    else:
        miFormulario = empleadosFormulario()
    return render(request, "AgenciApp/setEmpleadosVendedores.html", {"miFormulario":miFormulario, "Empleados":Empleados})

def eliminarEmpleadoVendedor(request, email_empleado):
    empleado = empleadosVendedores.objects.get(email = email_empleado)
    empleado.delete()
    miFormulario = empleadosFormulario()
    Clientes = empleadosVendedores.objects.all()
    return redirect('setEmpleadosVendedores')

def editarEmpleadoVendedor(request, email_empleado):
    empleado = empleadosVendedores.objects.get(email = email_empleado)
    if request.method == 'POST':
        miFormulario = empleadosFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            empleado.nombre = data['nombre']
            empleado.apellido = data['apellido']
            empleado.email = data['email']
            empleado.celular = data['celular']
            empleado.operacionesConcretadas = data['operacionesConcretadas']
            empleado.montoVendido = data['montoVendido']
            empleado.save()

            miFormulario = empleadosVendedores.objects.all()
            return redirect('setEmpleadosVendedores')
    else:
        miFormulario = empleadosFormulario(initial={'nombre': empleado.nombre, 'apellido': empleado.apellido, 'email': empleado.email, 'celular': empleado.celular, 'operacionesConcretadas': empleado.operacionesConcretadas, 'montoVendido': empleado.montoVendido})

    return render(request, "AgenciApp/editarEmpleadosVendedores.html", {"miFormulario": miFormulario})

#########################################################################################################################

