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
    autoComprado = forms.CharField(label='Auto Comprado')
    montoOperacionComp = forms.IntegerField(label='Monto Compra')

class clientesVendFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    celular = forms.IntegerField()
    autoVendido = forms.CharField(label='Auto Vendido')
    montoOperacionVent = forms.IntegerField(label='Monto Venta')    

class empleadosFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    celular = forms.IntegerField()
    operacionesConcretadas = forms.CharField(label='Operaciones Concretadas')
    montoVendido = forms.IntegerField(label='Monto Vendido')