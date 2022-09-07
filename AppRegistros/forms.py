from django import forms

class RegistroFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()


class BusquedaFormulario(forms.Form):
    camada = forms.IntegerField()
