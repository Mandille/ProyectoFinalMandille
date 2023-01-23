from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    imagen = models.ImageField(upload_to='avatar')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
