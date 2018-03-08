from django.db import models

# Create your models here.

#CREAMOS EL MODELO PERSONA
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(max_length=70)
    direccion = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_nac = models.DateField()

    def __str__(self):
        completo = self.nombre +" "+self.apellidos
        return completo

#CREAR MODELO GRUPO
class Grupo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

#CREAR MODELO CONTACTO
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    telefono = models.IntegerField()
    fijo = models.IntegerField()
    correo = models.EmailField(max_length=70)
    direccion = models.CharField(max_length=100)
    #Relacion quiere decir que una persona puede tener varios contactos
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    # Relacion quiere decir que una persona puede pertenecer a varios grupos
    grupo = models.ManyToManyField(Grupo, blank=True, null=True)
    def __str__(self):
        completo= self.nombre +" "+self.apellidos
        return completo


