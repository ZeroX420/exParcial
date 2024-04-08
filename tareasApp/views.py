from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import tareas

# Create your views here.

def indice(request):

    tareasTotales = tareas.objects.all()
    return render(request, 'indice.html', {

        'tareasTotales': tareasTotales

    })

def nuevaTarea(request):

    if request.method == 'POST':

        print(request.POST)
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        fechaFin = request.POST.get('fechaFin')
#        estadoTarea = request.POST.get('estadoTarea')
        estadoTarea = 'EN PROGRESO'
        responsableTarea = request.POST.get('responsableTarea')

        tareaCreada = tareas.objects.create(

            nombre = nombre,
            descripcion = descripcion,
            fechaFin = fechaFin,
            estadoTarea = estadoTarea,
            responsableTarea = responsableTarea

        )

        return HttpResponseRedirect(reverse('tareasApp:indice'))
    
    return render(request, 'nuevaTarea.html')