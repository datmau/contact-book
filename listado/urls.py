from django.contrib import admin
from django.urls import path, include

from listado.views import lista_contactos,persona_contactos,DetalleContacto, CrearContacto, EditarContacto

app_name = 'listado'
urlpatterns = [
    path('contactos/', lista_contactos, name='contacto_lista'),
    path('personas/', persona_contactos),
    path('contactos/<int:pk>', DetalleContacto.as_view(), name='contacto_detalle'),
    path('contactos/nuevo', CrearContacto.as_view(), name='contacto_crear'),
    path('contactos/editar/<int:pk>', EditarContacto.as_view(), name='contacto_editar'),

]