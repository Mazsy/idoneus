
from django.shortcuts import render
from .forms import RegistrarUsuario

def index(request):
    register_form = RegistrarUsuario()
    return render(request, 'forms/mi_form.html', {'register_form': register_form})