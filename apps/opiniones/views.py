from typing import Any
from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import OpinionForm
from .models import Opinion
# Create your views here.
def AgregarOpinion(request):
    form = OpinionForm(request.POST or None)
    if form.is_valid():
        form.save()

    contexto = {
        'form': form,
    }
    template_name = 'opiniones/agregar_opinion.html'
    return render(request, template_name, contexto)

class ModificarOpinion(LoginRequiredMixin, UpdateView):
    model = Opinion
    fields = ['texto']
    template_name = 'opiniones/modificar_opinion.html'
    success_url = reverse_lazy('apps.empleos:listar_empleos')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(usuario = self.request.user)

class EliminarOpinion(LoginRequiredMixin, DeleteView):
    model = Opinion
    template_name = 'opiniones/confirmar_eliminacion.html'
    success_url = reverse_lazy('apps.empleos:listar_empleos')