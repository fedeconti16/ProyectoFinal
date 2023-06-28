from django.http import HttpResponse
from django.template import Template, Context, loader

#def saludo(request):
#    return HttpResponse("Hola Djangooooo")
#
#def probandoTemplate(self):
#    nombre = "Leo" 
#    apellido = "Messi"
#
#    namelist = ["Gabriel", "Jimena", "Nacho", "Patricia", "Natalia"]
#    
#    diccionario = {
#        "nombre": nombre,
#        "apellido": apellido,
#        "namelist": namelist
#    }
#
#    plantilla = loader.get_template("template1.html")
#    documento = plantilla.render(diccionario)
#    return HttpResponse(documento)