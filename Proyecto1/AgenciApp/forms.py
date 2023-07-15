from django import forms  
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User 

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
 
class UserEditForm(UserChangeForm):
    username = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Email"}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"First Name"}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Last Name"}))
    password = None

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}
    
            

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label = "", widget= forms.PasswordInput(attrs={"placeholder":"Contraseña Actual"}))
    new_password1 = forms.CharField(label = "", widget= forms.PasswordInput(attrs={"placeholder":"Nueva Contraseña"}))
    new_password2 = forms.CharField(label = "", widget= forms.PasswordInput(attrs={"placeholder":"Confirmar Contraseña"}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:"" for k in fields}

