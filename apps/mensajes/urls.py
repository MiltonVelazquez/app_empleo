from django.urls import path
from .views import *

app_name = 'apps.mensajes'

urlpatterns = [
    path("contacto/", AgregarMensaje,name='agregar_mensaje'),
    path('mensajes/', ListarMensajes.as_view(), name='listar_mensajes'),
]
