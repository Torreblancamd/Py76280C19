from django import forms


class Curso_formulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    camada = forms.IntegerField()