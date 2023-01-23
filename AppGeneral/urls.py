from django.urls import path
from .views import *
from django.contrib.auth. views import LogoutView


urlpatterns = [

    path('', inicio, name='inicio'),

    path('reviews', reviews, name='reviews'),
    path('review_formulario/', review_formulario, name='review_formulario'),
    path('review_listados/', review_listados, name='review_listados'),
    path('review_mostrar/<id>', review_mostrar, name='review_mostrar'),
    path('review_borrar/<id>', review_borrar, name='review_borrar'),
    path('review_editar/<id>', review_editar, name='review_editar'),

    path('about/', about, name='about'),

]