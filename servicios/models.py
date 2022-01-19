from django.db import models

# Create your models here.

class servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='servicios') #cuando alzamos multimedia le decimos que almacene en la carpeta media creando una sub carpeta servicios y que guarde ahi
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo