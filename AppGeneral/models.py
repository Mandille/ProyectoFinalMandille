from django.db import models

class Review(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=50)
    fecha =  ()
    imagen = models.ImageField(upload_to='Img_Post')
    
    def __str__(self):
        return self.titulo

#Ok


