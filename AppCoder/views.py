from django.shortcuts import render # type: ignore
from django.http import HttpResponse
from AppCoder.models import Curso
from django.template import loader
# Create your views here.



def inicio(request):
    return render(request, "padre.html")


def cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos":cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento)



def alta_curso(request, nombre):
    curso = Curso(nombre=nombre , camada=99999)
    curso.save()
    msj = f"Se guardo el curso {curso.nombre} {curso.camada}"
    return HttpResponse(msj)



def profesores(request):
    return render(request, "profesores.html")


def alumnos(request):
    return render(request, "alumnos.html")



def contacto(request):
    return render(request, "contacto.html")

