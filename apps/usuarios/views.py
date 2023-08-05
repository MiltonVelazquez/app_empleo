from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Usuarios
from .forms import RegistrarUsuariosForm
# Create your views here.
class RegistrarUsuario(CreateView):
    model = Usuarios
    template_name = 'usuarios/registrar.html'
    form_class = RegistrarUsuariosForm
    success_url = reverse_lazy('inicio')

class EliminarUsuario(LoginRequiredMixin, DeleteView):
    model = Usuarios
    template_name = 'usuarios/confirmar_eliminacion.html'
    success_url = reverse_lazy('apps.usuarios:listar_usuarios')

class ModificarUsuario(LoginRequiredMixin, UpdateView):
    model = Usuarios
    fields = fields = ['nombre','apellido','dni','fecha_nacimiento','username','email','imagen']
    template_name = 'usuarios/registrar.html'
    success_url = reverse_lazy('inicio')

def ListarUsuarios(request):
    usuarios = Usuarios.objects.all()
    template_name = 'usuarios/listar_usuarios.html'
    contexto = {
        "usuarios":usuarios
    } 
    return render(request, template_name, contexto)