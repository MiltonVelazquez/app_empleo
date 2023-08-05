from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import AgregarCategoria, AgregarEmpleos, EliminarEmpleo, ListarEmpleos, ListarEmpleosPorCategoria, empleo_detalle, OrdenarEmpleosPor

app_name = 'apps.empleos'

urlpatterns = [
    path("agregar_categoria/", AgregarCategoria.as_view(),name='agregar_categoria'),
    path("agregar_empleo/", AgregarEmpleos.as_view(),name='agregar_empleo'),
    path("modificar_empleo/<int:pk>", ModificarEmpleo.as_view(), name='modificar_empleo'),
    path("eliminar_empleo/<int:pk>", EliminarEmpleo.as_view(), name='eliminar_empleo'),
    path("listar_empleos/", ListarEmpleos.as_view(), name='listar_empleos'),
    path("listar_por_categoria/<str:categoria>", ListarEmpleosPorCategoria, name='listar_por_categoria'),
    path("empleo_detalle/<int:id>", empleo_detalle, name='empleo_detalle'),
    path("ordenar_por/",OrdenarEmpleosPor, name='ordenar_por'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)