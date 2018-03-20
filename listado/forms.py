from django import forms
from listado.models import Contacto

class ContactoCrearForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = [
            'nombre',
            'apellidos',
            'foto',
            'correo',
            'direccion',
            'telefono',
            'fijo',
            'persona',
            'grupo',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'foto': 'Imagen',
            'correo': 'Correo',
            'direccion': 'Direccion',
            'telefono': 'Celular',
            'fijo': 'Fijo',
            'persona': 'Pertenece a',
            'grupo': 'Grupo/s',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'fijo': forms.TextInput(attrs={'class': 'form-control'}),
            'persona': forms.Select(attrs={'class': 'form-control'}),
            'grupo': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        }


