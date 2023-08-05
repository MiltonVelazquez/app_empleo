from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Categoria, Empleos
from apps.opiniones.models import Opinion
from apps.opiniones.forms import OpinionForm
# Create your views here.
class AgregarCategoria(LoginRequiredMixin, CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'empleos/agregar_categoria.html'
    success_url = reverse_lazy('inicio')
    
    template_name = 'empleos/agregar_categoria.html' 

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        nombre_ingresado = request.POST.get('nombre') 
        if Categoria.objects.filter(nombre=nombre_ingresado).exists():
            error_msg = 'El valor ya existe en la base de datos.'
            return render(request, self.template_name, {'error_msg': error_msg})
        nuevo_objeto = Categoria(nombre=nombre_ingresado)
        nuevo_objeto.save()

        return redirect('inicio')
    
class AgregarEmpleos(LoginRequiredMixin, CreateView):
    model = Empleos
    fields = ['titulo', 'nombre_empresa','descripcion','imagen','categoria']
    template_name = 'empleos/agregar_empleo.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.colaborador = self.request.user
        return super().form_valid(form)

class ModificarEmpleo(LoginRequiredMixin, UpdateView):
    model = Empleos
    fields = ['titulo', 'nombre_empresa','descripcion','imagen','categoria']
    template_name = 'empleos/agregar_empleo.html'
    success_url = reverse_lazy('apps.empleos:listar_empleos')

class EliminarEmpleo(LoginRequiredMixin, DeleteView):
    model = Empleos
    template_name = 'empleos/confirmar_eliminacion.html'
    success_url = reverse_lazy('apps.empleos:listar_empleos')


class ListarEmpleos(ListView):
    model = Empleos
    template_name = 'empleos/listar_empleos.html'
    context_object_name = 'empleos'#Recolecta todos los objetos de empleos
    #GetQuery
    paginate_by = 9

    def get_context_data(self):
        context = super().get_context_data()#Vuelve a recolectar los objetos para esta clase
        categorias = Categoria.objects.all()#Recolecta los objetos de categorias
        context['categorias'] = categorias#Añade los objetos de categorias a los objetos de empleo
        return context
    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get('buscador')
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(titulo__icontains=query)
        return queryset.order_by('titulo')

def ListarEmpleosPorCategoria(request, categoria):
    categorias2 = Categoria.objects.filter(nombre = categoria)
    empleos = Empleos.objects.filter(categoria =categorias2[0].id).order_by('fecha_agregado')
    categorias = Categoria.objects.all()
    template_name = 'empleos/listar_empleos.html'
    contexto = {
        'empleos':empleos,
        'categorias':categorias
    }
    return render(request, template_name, contexto)
    
def empleo_detalle(request, id):
    empleos = Empleos.objects.get(id=id)
    opiniones = Opinion.objects.filter(empleo=id)
    form = OpinionForm(request.POST)

    if form.is_valid():
        if request.user.is_authenticated:
            aux = form.save(commit=False)
            aux.empleo = empleos
            aux.usuario = request.user
            aux.save()
            form = OpinionForm()
        else:
            return redirect('apps.usuarios:iniciar_sesion')

    contexto = {
        'empleo': empleos,
        'form': form,
        'opiniones': opiniones,
    }
    template_name = 'empleos/empleo.html'
    return render(request, template_name, contexto)

def OrdenarEmpleosPor(request):
    orden = request.GET.get('orden', '')
    if orden == 'fecha':
        empleos = Empleos.objects.order_by('fecha_agregado')
    elif orden == 'titulo':
        empleos = Empleos.objects.order_by('titulo')
    elif orden == 'des_fecha':
        empleos = Empleos.objects.order_by('-fecha_agregado')
    elif orden == 'des_titulo':
        empleos = Empleos.objects.order_by('-titulo')
    else:  
        empleos = Empleos.objects.all()  

    context = {
        'empleos': empleos,
    }
    return render(request, 'empleos/listar_empleos.html', context)

def inicio(request):
    empleos_recientes = Empleos.objects.order_by('-fecha_agregado')[:3]
    context = {
        'empleos_recientes' : empleos_recientes
        }

    return render(request, 'inicio.html', context)