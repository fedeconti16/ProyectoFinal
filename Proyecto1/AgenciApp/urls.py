from django.urls import path
from AgenciApp.views import *

urlpatterns = [
    path('inicio/', inicio),
    path('autosEnStock/', AutosEnStock, name="autosEnStock"),
    path('clientesCompradores/', ClientesCompradores, name="clientesCompradores"),
    path('clientesVendedores/', ClientesVendedores, name="clientesVendedores"),
    path('empleadosVendedores/', EmpleadosVendedores, name="empleadosVendedores"),
    #path('setAutosEnStock/', setAutosEnStock, name="setAutosEnStock"),

]