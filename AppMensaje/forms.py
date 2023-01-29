from django import forms
from django.contrib.auth.models import User
from datetime import datetime

class Form_Mensaje(forms.Form):
    receptor = forms.ChoiceField(label='receptor', choices=[(user.username, user.username) for user in User.objects.all()],)    
    mensaje = forms.CharField(label="cuerpo", widget=forms.Textarea,)
    fecha = forms.DateTimeField(label="fecha", initial=datetime.now())