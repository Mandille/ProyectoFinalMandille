from django.shortcuts import render
from django.http import HttpResponse
from .models import Review

from AppRegistro.views import generar_avatar
from AppGeneral.forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio (request):
    return render(request, 'AppGeneral/inicio.html')

def reviews (request):
    return render(request, 'AppGeneral/reviews.html')    

def review_listados (request):
    review = Review.objects.all()
    if len(review) != 0:
        return render(request, 'AppGeneral/review_listados.html', {'reviews': reviews})
    else:
        return render(request, 'AppGeneral/review_listados.html', {'mensaje': 'Aún no hay reseñas realizadas, crea la primera!'}) 

@login_required
def review_formulario (request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
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
            
            return render(request, 'AppGeneral/review_mostrar.html', {'review': review, 'avatar': generar_avatar(request)})
        else:
            return render(request, 'AppGeneral/review_formulario.html', {'form': form, 'avatar': generar_avatar(request)})
    else:
        form = ReviewForm()
        return render(request, 'AppGeneral/review_formulario.html', {'form': form, 'avatar': generar_avatar(request)})

def review_mostrar(request, id):
    review = Review.objects.get(id=id)
    return render(request, 'AppGeneral/review_mostrar.html', {'review': review})

# Editar posteo

@login_required
def review_editar (request, id):
    review = Review.objects.get(id=id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
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
            return render(request, 'AppGeneral/review_listados.html', {'mensaje': 'La reseña ha sido modificada', 'reviews': reviews, 'avatar': generar_avatar(request)})        
    else:
        form = ReviewForm(initial={'titulo': review.titulo, 'subtitulo': review.subtitulo, 'cuerpo': review.cuerpo, 'autor': review.autor, 'fecha': review.fecha, 'imagen': review.imagen})
        return render(request, 'AppGeneral/review_editar.html', {'form': form, 'review': review, 'avatar': generar_avatar(request)})

#Eliminar posteo

@login_required
def review_borrar (request, id):
    review = Review.objects.get(id=id)
    review.delete()
    return render(request, 'AppGeneral/review_borrar.html', {'mensaje': 'La reseña ha sido eliminada', 'avatar': generar_avatar(request)})

#About

def about (request):
    return render(request, 'AppGeneral/about.html')
