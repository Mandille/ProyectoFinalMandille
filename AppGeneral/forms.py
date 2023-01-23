from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class ReviewForm(forms.Form):
    titulo = forms.CharField(label="titulo", max_length=50)
    subtitulo = forms.CharField(label="subtitulo", max_length=50)
    cuerpo = forms.CharField(label="cuerpo", widget=forms.Textarea)
    autor = forms.CharField(label="autor", max_length=50)
    fecha = forms.DateField(label="fecha")
    imagen = forms.ImageField(label="imagen", required=False)   

#Ok
