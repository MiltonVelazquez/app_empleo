from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from apps.empleos.models import Empleos

# def inicio(request):
#     template_name = 'inicio.html'
#     return render(request, template_name)
def inicio(request):
    empleos_recientes = Empleos.objects.order_by('-fecha_agregado')[:3]
    context = {
        'empleos_recientes' : empleos_recientes
        }

    return render(request, 'inicio.html', context)

def contacto(request):
    template_name = 'contacto.html'
    return render (request, template_name)

def acercade(request):
    template_name = 'acercade.html'
    return render (request, template_name)

