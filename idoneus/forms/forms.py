from django import forms
from forms.models import Usuarios

class RegistrarUsuario(forms.Form):
	nombre = forms.CharField(label='Nombre:',max_length=15)
	telefono = forms.CharField(label='Teléfono',max_length=12)
	fecha_de_nacimiento = forms.DateField(label='Fecha nacimiento:')
	email = forms.EmailField(label='Email:',max_length=254)

	