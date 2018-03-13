from django.contrib import admin
from django.urls import path, include

from listado.views import lista_contactos,persona_contactos


urlpatterns = [
    path('contactos/', lista_contactos),
    path('personas/', persona_contactos),
]