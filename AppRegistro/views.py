from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import Avatar, Descripcion, Url
from AppRegistro.forms import Form_User_Registro, Form_User_Editar, Form_Avatar, Form_Descripcion, Form_Url
from django.contrib.auth.decorators import login_required

def avatar_obtener(request):
    lista = Avatar.objects.filter(usuario=request.user)
    if len(lista) != 0:
        avatar = lista[0].imagen.url
    else:
        avatar = '/Avatar/avatar/3161402.png'
    return avatar

@login_required
def avatar_agregar (request):
    if request.method == 'POST':
        form = Form_Avatar(request.POST, request.FILES)
        if form.is_valid():
            avatar = Avatar(usuario=request.user, imagen=request.FILES['imagen'])
            avatar_anterior= Avatar.objects.filter(usuario=request.user)
            if len(avatar_anterior)>0:
                avatar_anterior[0].delete()
            avatar.save()
            return render (request, 'AppGeneral/user_perfil.html', {'form': form, 'avatar': avatar_obtener(request), 'mensaje': 'Avatar añadido correctamente'})
        else:
            return render (request, 'AppGeneral/avatar_agregar.html', {'form': form, 'avatar': avatar_obtener(request), 'mensaje': 'Error. El avatar ha sido añadido correctamente'})
    else:
        form = Form_Avatar()
        return render(request, 'AppGeneral/avatar_agregar.html', {'form': form, 'avatar': avatar_obtener(request), 'mensaje': 'Agregar/Modificar avatar'})

def url_obtener(request):
    lista = Url.objects.filter(usuario=request.user)
    if len(lista) != 0:
        url = lista[0].url
    else:
        url = ''
    return url

@login_required
def url_agregar (request):
    if request.method == 'POST':
        form = Form_Url(request.POST)
        if form.is_valid():
            url = Url(usuario=request.user, url=request.POST['url'])
            url_anterior= Url.objects.filter(usuario=request.user)
            if len(url_anterior)>0:
                url_anterior[0].delete()
            url.save()
            return render (request, 'AppGeneral/user_perfil.html', {'form': form, 'avatar': url_obtener(request), 'url' : url_obtener(request), 'mensaje': 'URL añadido correctamente'})
        else:
            return render (request, 'AppGeneral/url_agregar.html', {'form': form, 'avatar': url_obtener(request), 'mensaje': 'Error. El URL no ha sido añadido correctamente'})
    else:
        form = Form_Url()
        return render(request, 'AppGeneral/url_agregar.html', {'form': form, 'avatar': url_obtener(request)})

def descripcion_obtener(request):
    lista = Descripcion.objects.filter(usuario=request.user)
    if len(lista) != 0:
        descripcion = lista[0].descripcion
    else:
        descripcion = ''
    return descripcion

@login_required
def descripcion_agregar (request):
    if request.method == 'POST':
        form = Form_Descripcion(request.POST)
        if form.is_valid():
            descripcion = Descripcion(usuario=request.user, descripcion=request.POST['descripcion'])
            descripcion_anterior= Descripcion.objects.filter(usuario=request.user)
            if len(descripcion_anterior)>0:
                descripcion_anterior[0].delete()
            descripcion.save()
            return render (request, 'AppGeneral/user_perfil.html', {'form': form, 'avatar': avatar_obtener(request), 'mensaje': 'Descripcion añadida correctamente', 'descripcion': descripcion_obtener(request)})
        else:
            return render (request, 'AppGeneral/descipcion_agregar.html', {'form': form, 'avatar': avatar_obtener(request), 'mensaje': 'Error. La descripción no ha sido añadida correctamente'})
    else:
        form = Form_Descripcion()
        return render(request, 'AppGeneral/descripcion_agregar.html', {'form': form, 'avatar': avatar_obtener(request)})

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
def user_perfil (request):
    usuario = request.user
    form = Form_User_Editar(instance=usuario)
    return render(request, 'AppGeneral/user_perfil.html', {'avatar': avatar_obtener(request), 'url' : url_obtener(request), 'descripcion': descripcion_obtener(request), 'form': form})


