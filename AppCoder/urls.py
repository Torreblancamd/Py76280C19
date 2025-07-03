from django.urls import path 
from . import views

urlpatterns=[
    path("", views.inicio),   
    path("alta_curso/<str:nombre>" , views.alta_curso),
    path("profesores", views.profesores , name="profesores"),
    path("alumnos", views.alumnos, name="alumnos"),
    path('cursos' , views.cursos, name="cursos"),
    path("contacto", views.contacto, name="contacto")
      
] 