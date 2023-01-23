from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import Avatar

from AppRegistro.forms import Form_User_Registro, Form_User_Editar
from django.contrib.auth.decorators import login_required

def generar_avatar(request):
    lista = Avatar.objects.filter(usuario=request.user)
    if len(lista) != 0:
        avatar = lista[0].imagen.url
    else:
        avatar = '/Avatar/avatar/3161402.png'
    return avatar

def user_registro(request):
    if request.method == 'POST':
        form= Form_User_Registro(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return render(request, 'AppGeneral/inicio.html', {'form': form, 'mensaje': 'Usuario registrado'})
        else:
            return render(request, 'AppGeneral/user_registro.html', {'form': form, 'mensaje': 'Usuario no registrado, intente nuevamente'})   
    else:
        form= Form_User_Registro()
        return render(request, 'AppGeneral/user_registro.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            informacion_usuario = form.cleaned_data
            username = informacion_usuario['username']
            password = informacion_usuario['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'AppGeneral/inicio.html', {'mensaje': f'{username}'})
            else:
                return render(request, 'AppGeneral/user_login.html', {'form': form, 'mensaje': 'El usuario y/o la contraseña son incorrectos, intente nuevamente'})
        else:
            return render(request, 'AppGeneral/user_login.html', {'form': form, 'mensaje': 'El usuario y/o la contraseña son incorrectos'})
    else:
        form= AuthenticationForm()
        return render(request, 'AppGeneral/user_login.html', {'form': form})

@login_required
def user_editar(request):
    user=request.user
    if request.method == 'POST':
        form = Form_User_Editar(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            user.first_name = info['first_name']
            user.last_name = info['last_name']
            user.email = info['email']
            user.password1 = info['password1']
            user.password2 = info['password2']
            user.save()
            return render(request, 'AppGeneral/inicio.html', {'mensaje': f'{user.username} ha sido modificado.'})
        else:
            return render(request, 'AppGeneral/user_editar.html', {'form': form, 'usuario': user.username})
    else:
        form = Form_User_Editar(instance=user)
        return render(request, 'AppGeneral/user_editar.html', {'form': form, 'usuario': user.username})