from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView
from listado.forms import ContactoCrearForm
from django.urls import reverse_lazy

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

class DetalleContacto(DetailView):
    model = Contacto
    template_name = 'detalle_contacto.html'

class CrearContacto(CreateView):
    model = Contacto
    form_class = ContactoCrearForm
    template_name = 'crear_contacto.html'
    success_url = reverse_lazy('listado:contacto_lista')



class EditarContacto(UpdateView):
    model = Contacto
    form_class = ContactoCrearForm
    template_name = 'crear_contacto.html'
    succes_url =  reverse_lazy('listado:contacto_lista')

