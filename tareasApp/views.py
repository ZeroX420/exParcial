from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

lista_tareas = [

    ['DESCANSAR', 'NECESITA REPOSO' ,'2024-03-30', 'EN PROGRESO', 'ALEXANDER']

]

# Create your views here.

def indice(request):
    return render(request, 'indice.html', {

        'lista_tareas': lista_tareas

    })

def nuevaTarea(request):

    if request.method == 'POST':

        print(request.POST)
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        fechaFin = request.POST.get('fechaFin')
        ##estadoTarea = request.POST.get('estadoTarea')
        responsableTarea = request.POST.get('responsableTarea')
        print(nombre)
        print(descripcion)
        print(fechaFin)
        ##print(estadoTarea)
        print(responsableTarea)
        lista_tareas.append([nombre, descripcion, fechaFin, 'EN PROGRESO', responsableTarea])
        return HttpResponseRedirect(reverse('tareasApp:indice'))
    
    return render(request, 'nuevaTarea.html')