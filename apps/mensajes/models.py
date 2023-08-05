from django.db import models
from apps.usuarios.models import Usuarios
# Create your models here.
class Mensaje(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    texto = models.TextField(verbose_name='Mensaje')
    fecha = models.DateTimeField(auto_now_add=True)
    asunto = models.TextField(max_length=50)
    imagen = models.ImageField(null=True,blank=True,upload_to='mensajes',default='empleos/empleo_def.png')

    def __str__(self):
        return self.texto
    
    class Meta:
        ordering = ['-fecha']