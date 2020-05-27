from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request, 'home/templates/index.html', {})

def oportunidades(request):
    data = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'home/templates/oportunidades.html', {'p': data})

def position (request, pk):
    position_object = Post.objects.get(pk=pk)
    return render(request, 'home/templates/posicion.html', {'data': position_object.text})

def facebook(request):
    return HttpResponseRedirect("https://www.facebook.com")

def gestionrrhh(request):
    return render(request, 'home/templates/Servicios/gestionrrhh.html', {})

def consultoria(request):
    return render(request, 'home/templates/Servicios/consultoria.html', {})

def intervencionesPsicolaborales(request):
    return render(request, 'home/templates/Servicios/intervencionesPsicolaborales.html', {})

def busquedayseleccion(request):
    return render(request, 'home/templates/Servicios/busquedayseleccion.html', {})

def seleccionit(request):
    return render(request, 'home/templates/Servicios/Seleccion_IT.html', {})
