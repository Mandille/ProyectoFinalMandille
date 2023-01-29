from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Form_User_Registro(UserCreationForm):
    first_name = forms.CharField(label='Nombre', max_length=50)
    last_name = forms.CharField(label='Apellido', max_length=50)
    email = forms.EmailField(label='Email', max_length=50)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields} 

class Form_User_Editar(UserCreationForm):
    first_name = forms.CharField(label='Nombre', max_length=50)
    last_name = forms.CharField(label='Apellido', max_length=50)
    email = forms.EmailField(label='Email', max_length=50)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        help_texts = {k:"" for k in fields} 

class Form_Avatar(forms.Form):
    imagen = forms.ImageField(label='Imagen')

class Form_Url(forms.Form):
    url = forms.URLField(label='URL', max_length=300)

    def __str__(self):
        return self.url

class Form_Descripcion(forms.Form):
    descripcion = forms.CharField(label='Descripcion', max_length=200, widget=forms.Textarea)