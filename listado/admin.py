from django.contrib import admin
from listado.models import Persona,Grupo,Contacto

# Register your models here.
#AQUI ES DONDE REGISTRAMOS LOS MODELOS QUE QUERRAMOS VER EN EL ADMINISTRADOR
admin.site.register(Persona)
admin.site.register(Grupo)
admin.site.register(Contacto)