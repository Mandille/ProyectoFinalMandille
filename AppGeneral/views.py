from django.shortcuts import render
from django.http import HttpResponse
from .models import Review
from PIL import Image

from AppRegistro.views import avatar_obtener
from AppGeneral.forms import Form_Review
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio (request):
    if request.user.is_authenticated:
        return render(request, 'AppGeneral/inicio.html', {'avatar': avatar_obtener(request)})
    else:
        return render(request, 'AppGeneral/inicio.html')

def reviews (request):
    if request.user.is_authenticated:
        return render(request, 'AppGeneral/reviews.html', {'avatar': avatar_obtener(request)})
    else:
        return render(request, 'AppGeneral/reviews.html')    

def review_listados (request):
    if request.user.is_authenticated:
        review = Review.objects.all()
        if len(review) != 0:
            return render(request, 'AppGeneral/review_listados.html', {'reviews': review, 'avatar': avatar_obtener(request)})
        else:
            return render(request, 'AppGeneral/review_listados.html', {'mensaje': 'Aún no hay reseñas realizadas, crea la primera!', 'avatar': avatar_obtener(request)}) 
    else:
        review = Review.objects.all()
        if len(review) != 0:
            return render(request, 'AppGeneral/review_listado.html', {'posteos': review})
        else:
            return render(request, 'AppGeneral/review_listado.html', {'mensaje': 'Aún no hay reseñas realizadas, crea la primera!'}) 

@login_required
def review_formulario (request):
    if request.method == 'POST':
        form = Form_Review(request.POST, request.FILES)
        if form.is_valid():
            info = form.cleaned_data
            titulo = info['titulo']
            subtitulo = info['subtitulo']
            cuerpo = info['cuerpo']
            autor = info['autor']
            fecha = info['fecha']
            imagen = info['imagen']
            review = Review(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha, imagen=imagen)
            review.save()
            
            return render(request, 'AppGeneral/review_mostrar.html', {'review': review, 'avatar': avatar_obtener(request)})
        else:
            return render(request, 'AppGeneral/review_formulario.html', {'form': form, 'avatar': avatar_obtener(request)})
    else:
        form = Form_Review()
        return render(request, 'AppGeneral/review_formulario.html', {'form': form, 'avatar': avatar_obtener(request)})

def review_mostrar(request, id):
    review = Review.objects.get(id=id)
    if request.user.is_authenticated:
        return render(request, 'AppGeneral/review_mostrar.html', {'post': review, 'avatar': avatar_obtener(request)})
    else:
        return render(request, 'AppGeneral/review_mostrar', {'post': review})

# Editar posteo

@login_required
def review_editar (request, id):
    review = Review.objects.get(id=id)
    if request.method == 'POST':
        form = Form_Review(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            review.titulo = info["titulo"]
            review.subtitulo = info['subtitulo']
            review.cuerpo = info['cuerpo']
            review.autor = info['autor']
            review.fecha = info['fecha']
            review.imagen = info['imagen']
            review.save()
            reviews = Review.objects.all()
            return render(request, 'AppGeneral/review_listados.html', {'mensaje': 'La reseña ha sido modificada', 'reviews': reviews, 'avatar': avatar_obtener(request)})        
    else:
        form = Form_Review(initial={'titulo': review.titulo, 'subtitulo': review.subtitulo, 'cuerpo': review.cuerpo, 'autor': review.autor, 'fecha': review.fecha, 'imagen': review.imagen})
        return render(request, 'AppGeneral/review_editar.html', {'form': form, 'review': review, 'avatar': avatar_obtener(request)})

#Eliminar posteo

@login_required
def review_borrar (request, id):
    review = Review.objects.get(id=id)
    if request.user.is_superuser:
        review.delete()
        return render(request, 'AppGeneral/review_borrar.html', {'mensaje': 'La reseña ha sido eliminada', 'avatar': avatar_obtener(request)})
    else:
        return render(request, 'AppGeneral/review_borrar.html', {'mensaje': 'Para eliminar esta reseña necesitas tener permiso.', 'avatar': avatar_obtener(request)})

#About

def about (request):
    if request.user.is_authenticated:
        return render(request, 'AppGeneral/about.html', {'avatar': avatar_obtener(request)})
    else:
        return render(request, 'AppGeneral/about.html')
