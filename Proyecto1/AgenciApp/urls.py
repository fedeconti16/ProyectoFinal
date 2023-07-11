from django.urls import path
from AgenciApp.views import *

urlpatterns = [
    path('inicio/', inicio),
#    path('autosEnStock/', AutosEnStock, name="autosEnStock"),
    path('clientesCompradores/', ClientesCompradores, name="clientesCompradores"),
    path('clientesVendedores/', ClientesVendedores, name="clientesVendedores"),
    path('empleadosVendedores/', EmpleadosVendedores, name="empleadosVendedores"),
    path('getAutosEnStock/', getAutosEnStock, name='getAutosEnStock'),
    path('buscarAutosEnStock/', buscarAutosEnStock, name='buscarAutosEnStock'),
    path('setAutosEnStock/', setAutosEnStock, name='setAutosEnStock'),
    path('eliminarAuto/<marca_auto>/<modelo_auto>/', eliminarAuto, name='eliminarAuto'),
]