from django import forms   

class autosFormulario(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    km = forms.IntegerField()
    precio = forms.IntegerField()

