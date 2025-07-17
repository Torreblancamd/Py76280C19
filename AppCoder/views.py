from django.shortcuts import render # type: ignore
from django.http import HttpResponse
from AppCoder.models import Curso
from django.template import loader
from AppCoder.forms import Curso_formulario, UserEditForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required
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


@login_required
def profesores(request):
    return render(request, "profesores.html")


def alumnos(request):
    return render(request, "alumnos.html")



def contacto(request):
    return render(request, "contacto.html")




def curso_formulario(request):

    if request.method == "POST":
        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            curso = Curso( nombre=datos['nombre'] , camada=datos['camada'])
            curso.save()

            return render( request , "padre.html")                 
        
    
    return render( request , "formulario.html")






def buscar_curso(request):
    return render(request , "buscar_curso.html")

def buscar(request):
    
    if request.POST["nombre"]:
        cursos = Curso.objects.filter(nombre__icontains=request.POST["nombre"])
        return render(request, "resultado_busqueda.html", {"cursos":cursos})
    else:
        return HttpResponse("No se ha encontrado nada")
    


def eliminar_curso(request, id):
    
    curso = Curso.objects.get(id=id)
    curso.delete()

    curso = Curso.objects.all()

    return render(request, "cursos.html" , {"cursos":curso})




def editar( request , id ):

    curso = Curso.objects.get(id=id) 
    
    if request.method == "POST":
        mi_formulario = Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos['nombre']
            curso.camada = datos['camada']
            curso.save()

            curso = Curso.objects.all()
            return render(request , "cursos.html" , {"cursos":curso})


    else:
        mi_formulario = Curso_formulario(initial={'nombre':curso.nombre, 'camada':curso.camada})

    return render(request , "editar_curso.html" , {"mi_formulario":mi_formulario, "curso":curso })
       



def login_request(request):

    if request.method == "POST":
        
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

                usuario = form.cleaned_data.get("username")
                contra =  form.cleaned_data.get("password")

                user = authenticate(username=usuario, password=contra)

                if user is not None:
                    login(request,user)
                    return render(request, "inicio.html", {"mensaje":f"Bienvenido {usuario}"})
                else:
                    return render(request, "error.html", {"mensaje":f"Usuario no encontrado: {usuario}"})


    form = AuthenticationForm()

    return render(request, "login.html", {"form":form})





def register(request):

    if request.method == "POST":
       
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado exitosamente")
    else:
        form = UserCreationForm()
    return render(request, "registro.html", {"form":form})




@login_required
def editarPerfil( request ):

    usuario = request.user

    if request.method == "POST":
        
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()

            return render(request, "inicio.html")            


    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
    
    return render(request, "editar_perfil.html" ,{"miFormulario":miFormulario, "usuario":usuario})