from django import forms

class ClientesFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellidos = forms.CharField(max_length=40)
    telefono = forms.IntegerField()
    email = forms.EmailField()


class BusquedaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
