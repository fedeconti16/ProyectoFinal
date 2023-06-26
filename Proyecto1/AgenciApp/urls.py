from django.urls import path
from AgenciApp.views import *

urlpatterns = [
    path('inicio/', inicio),
    path('autosEnStock/', autosEnStock, name="autosEnStock"),
    path('clientesCompradores/', clientesCompradores, name="clientesCompradores"),
    path('clientesVendedores/', clientesVendedores, name="clientesVendedores"),
    path('empleadosVendedores/', empleadosVendedores, name="empleadosVendedores"),
#    path('getEstudiantes/', getEstudiantes, name="getEstudiantes"),
#    path('buscarEstudiante/', buscarEstudiante, name="buscarEstudiante"),

]