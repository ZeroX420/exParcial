from django.urls import path
from . import views

app_name = 'tareasApp'

urlpatterns = [

    path('', views.indice, name='indice'),
    path('nuevaTarea', views.nuevaTarea, name='nuevaTarea'),
]