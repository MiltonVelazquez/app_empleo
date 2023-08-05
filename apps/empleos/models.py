from django.db import models
from apps.usuarios.models import Usuarios
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=20,null=False)

    def __str__(self):
        return self.nombre

class Empleos(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    nombre_empresa = models.CharField(max_length=25, null=False)
    descripcion = models.TextField()
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    colaborador = models.ForeignKey(Usuarios, on_delete=models.SET_NULL,null=True, default=1)
    published = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(null=True,blank=True,upload_to='empleos',default='empleos/empleo_def.png')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    localidad = models.CharField(max_length=50, null=False, default='No aclarado')
    modalidad = models.CharField(max_length=50, null=False, default='No aclarado')
    direccion = models.CharField(max_length=50, null=False,default='No aclarado')
    numero = models.CharField(max_length=20, null=False, default='0000000000')

    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ('-published',)#Ordena de forma descendente al published, que es la fecha que se realiza la peticion