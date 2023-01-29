from django.shortcuts import render
from .models import Mensaje
from .forms import Form_Mensaje
from django.contrib.auth.decorators import login_required
from AppRegistro.views import avatar_obtener

@login_required
def mensajes(request):
    return render(request, 'AppGeneral/mensajes.html', {'avatar': avatar_obtener(request)})

@login_required
def mensaje_casilla(request):
    if request.user.is_authenticated:
        mensajes = Mensaje.objects.filter(receptor=request.user)
        if len(mensajes) != 0:
            return render(request, 'AppGeneral/mensaje_casilla.html', {'mensajes': mensajes, 'avatar': avatar_obtener(request)})
        else:
            return render(request, 'AppGeneral/mensaje_casilla.html', {'mensaje': 'No hay mensajes para mostrar', 'avatar': avatar_obtener(request)})

@login_required
def mensaje_enviar(request):
    if request.method == 'POST':
        form = Form_Mensaje(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            emisor = request.user
            receptor = informacion['receptor']
            mensaje = informacion['mensaje']
            fecha = informacion['fecha']
            mensaje = Mensaje(emisor=emisor, receptor=receptor, mensaje=mensaje, fecha=fecha)
            mensaje.save()
            return render(request, 'AppGeneral/inicio.html', {'mensaje': 'El mensaje ha sido enviado correctamente', 'avatar': avatar_obtener (request)})
        else:
            return render(request, 'AppGeneral/mensaje_enviar.html', {'form': form, 'mensaje': 'El mensaje no ha sido enviado', 'avatar': avatar_obtener (request)})
    else:
        form = Form_Mensaje()
        return render(request, 'AppGeneral/mensaje_enviar.html', {'form': form, 'avatar': avatar_obtener(request)})

@login_required
def mensaje_mostrar(request, id):
    mensaje = Mensaje.objects.get(id=id)
    mensaje.leido = True
    mensaje.save()
    return render(request, 'AppGeneral/mensaje_mostrar.html', {'mensaje': mensaje, 'avatar': avatar_obtener(request)})

@login_required
def mensaje_responder(request, id):
    mensaje = Mensaje.objects.get(id=id)
    if request.method == 'POST':
        form = Form_Mensaje(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            emisor = request.user
            receptor = informacion['receptor']
            mensaje = informacion['mensaje']
            fecha = informacion['fecha']
            mensaje = Mensaje(emisor=emisor, receptor=receptor, mensaje=mensaje, fecha=fecha)
            mensaje.save()
            return render(request, 'AppGeneral/inicio.html', {'mensaje': 'El mensaje ha sido enviado correctamente', 'avatar': avatar_obtener(request)})
        else:
            return render(request, 'AppGeneral/mensaje_enviar.html', {'form': form, 'mensaje': 'El mensaje no ha sido enviado', 'avatar': avatar_obtener(request)})
    else:
        form = Form_Mensaje()
        return render(request, 'AppGeneral/mensaje_enviar.html', {'form': form, 'mensaje': mensaje, 'avatar': avatar_obtener(request)})

@login_required
def mensaje_eliminar(request, id):
    mensaje = Mensaje.objects.get(id=id)
    mensaje.delete()
    return render(request, 'AppGeneral/inicio.html', {'mensaje': 'El mensaje ha sido eliminado correctamente', 'avatar': avatar_obtener(request)})