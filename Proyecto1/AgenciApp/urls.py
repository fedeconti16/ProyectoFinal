from django.urls import path
from AgenciApp.views import *

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('setAutosEnStock/', setAutosEnStock, name='setAutosEnStock'),
    path('eliminarAuto/<marca_auto>/<modelo_auto>/', eliminarAuto, name='eliminarAuto'),
    path('editarAuto/<marca_auto>/<modelo_auto>/', editarAuto, name='editarAuto'),
    path('setClientesCompradores/', setClientesCompradores, name='setClientesCompradores'),
    path('eliminarClienteComprador/<email_cliente>/', eliminarClienteComprador, name='eliminarClienteComprador'),
    path('editarClienteComprador/<email_cliente>/', editarClienteComprador, name='editarClienteComprador'),
    path('setClientesVendedores/', setClientesVendedores, name='setClientesVendedores'),
    path('eliminarClienteVendedor/<email_cliente>/', eliminarClienteVendedor, name='eliminarClienteVendedor'),
    path('editarClienteVendedor/<email_cliente>/', editarClienteVendedor, name='editarClienteVendedor'),
    path('setEmpleadosVendedores/', setEmpleadosVendedores, name='setEmpleadosVendedores'),
    path('eliminarEmpleadoVendedor/<email_empleado>/', eliminarEmpleadoVendedor, name='eliminarEmpleadoVendedor'),
    path('editarEmpleadoVendedor/<email_empleado>/', editarEmpleadoVendedor, name='editarEmpleadoVendedor'),

]