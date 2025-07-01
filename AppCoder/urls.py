from django.urls import path 
from . import views

urlpatterns=[
    path('cursos' , views.cursos),
    path("alta_curso/<str:nombre>" , views.alta_curso),
    path("profesores", views.profesores),
    path("alumnos", views.alumnos)
      
] 