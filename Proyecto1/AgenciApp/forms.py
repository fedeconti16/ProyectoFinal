from django import forms   

class autosFormulario(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    km = forms.IntegerField()
    precio = forms.IntegerField()

class clientesFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    celular = forms.IntegerField()
    autoComprado = forms.CharField()
    montoOperacionComp = forms.IntegerField()

class clientesVendFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    celular = forms.IntegerField()
    autoVendido = forms.CharField()
    montoOperacionVent = forms.IntegerField()    

class empleadosFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    celular = forms.IntegerField()
    operacionesConcretadas = forms.CharField()
    montoVendido = forms.IntegerField()