from django.shortcuts import render

from listado.models import Contacto,Persona
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def lista_contactos(request):
    contexto = Contacto.objects.all()
    return render(request, 'lista_contactos.html', {'contactos':contexto})

def persona_contactos(request):
    context = Contacto.objects.filter(id=3)
    return render(request, 'persona_contactos.html', {'contactos':context})