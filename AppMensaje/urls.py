from django.urls import path
from .views import *

urlpatterns = [
    path('mensajes/', mensajes, name='mensajes'),
    path('mensaje_casilla/', mensaje_casilla, name='mensaje_casilla'),
    path('mensaje_enviar/', mensaje_enviar, name='mensaje_enviar'),
    path('mensaje_mostar/<id>', mensaje_mostrar, name='mensaje_mostrar'),
    path('mensjar_responder/<id>', mensaje_responder, name='mensaje_responder'),
    path('mensaje_eliminar/<id>', mensaje_eliminar, name='mensaje_eliminar'),
]