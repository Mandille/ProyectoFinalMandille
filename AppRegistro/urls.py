from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('user_registro/', user_registro, name='user_registro'),
    path('user_editar/', user_editar, name='user_editar'),
    path('user_login/', user_login, name='user_login'),
    path('user_logout/', LogoutView.as_view(), name='user_logout'),
]