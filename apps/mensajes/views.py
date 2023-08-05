from django.shortcuts import render
from .forms import MensajeForm
from .models import Mensaje
from django.views.generic import ListView
# Create your views here.
def AgregarMensaje(request):
    form = MensajeForm(request.POST or None)
    if form.is_valid():
        form.instance.usuario = request.user
        form.save()

    contexto = {
        'form':form,
    }
    template_name = 'mensajes/contacto.html'
    return render(request, template_name, contexto)


class ListarMensajes(ListView):
    model = Mensaje
    template_name = 'mensajes/listar_mensajes.html'
    context_object_name = 'mensaje'#Recolecta todos los objetos de empleos
    #GetQuery
    paginate_by = 5