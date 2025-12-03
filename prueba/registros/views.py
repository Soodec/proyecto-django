from django.shortcuts import render
from .forms import ComentarioContactoForm
from .models import ComentarioContacto
from django.shortcuts import get_object_or_404
from .models import Alumnos
import datetime 
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages

# Create your views here.

def contacto(request):
    return render (request, "registros/contacto.html")

def registrarF(request):
    if request.method=='POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registros/comentarios_contacto.html')
    form = ComentarioContactoForm()
    return render (request, 'registros/contacto.html',{'form':form})

def principal(request):
    return render(request, "registros/principal.html")

def comentarios_contacto(request):
    comentarios = ComentarioContacto.objects.all()  # consulta con .all()
    return render(request, "registros/comentarios_contacto.html", {
        "comentarios": comentarios
    })

def eliminarComentarioContacto(request, id,
    confirmacion = 'registros/confirmacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request, "registros/comentarios_contacto.html", {
            "comentarios": comentarios
        })
    return render(request, confirmacion, {'object':comentario})

def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
    #get permite establecer una condicionante a la consulta y recupera el objetos
    #del modelo que cumple la condición (registro de la tabla ComentariosContacto.
    #get se emplea cuando se sabe que solo hay un objeto que coincide con su
    #consulta.
    return render(request,"registros/formEditarComentario.html",
    {'comentario':comentario})
    #Indicamos el lugar donde se renderizará el resultado de esta vista
    # y enviamos la lista de alumnos recuparados.
    
def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    #Referenciamos que el elemento del formulario pertenece al comentario
    # ya existente
    if form.is_valid():
        form.save() #si el registro ya existe, se modifica.
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/comentarios_contacto.html",
            {'comentarios':comentarios})
    #Si el formulario no es valido nos regresa al formulario para verificar
    #datos
    return render(request,"registros/formEditarComentario.html",
    {'comentario':comentario})
    
    
def consultas1(request):
    alumnos=Alumnos.objects.filter(carrera='TI')
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


def consultas2(request):
    alumnos=Alumnos.objects.filter(carrera='TI').filter(turno='MATUTINO')
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


def consultas3(request):
    alumnos=Alumnos.objects.all().only('matricula','nombre','carrera','turno','imagen')
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultas4(request):
    alumnos=Alumnos.objects.filter(turno__contains='VESPERTIN')
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultas5(request):
    alumnos=Alumnos.objects.filter(nombre__in=['Juan',"Ana"])
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultas6(request):
    fechaInicio=datetime.date(2025,10,1)
    fechaFin=datetime.date(2025,12,31)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultas7(request):
    alumnos=Alumnos.objects.filter(comentario__coment__contains='No inscrito')
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultas8(request):
    fechaInicio = datetime.date(2025, 11, 20)
    fechaFin = datetime.date(2025, 11, 26)
    comentarios = ComentarioContacto.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, "registros/consultas.html", {'comentarios': comentarios})

def consultas9(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__contains="hola")
    return render(request, "registros/consultas.html", {'comentarios': comentarios})

def consultas10(request):
    comentarios = ComentarioContacto.objects.filter(usuario="Juan")
    return render(request, "registros/consultas.html", {'comentarios': comentarios})

def consultas11(request):
    comentarios = ComentarioContacto.objects.values_list("mensaje", flat=True)
    return render(request, "registros/consultas.html", {'comentarios': comentarios})

def consultas12(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__startswith="A")
    return render(request, "registros/consultas.html", {'comentarios': comentarios})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion,
            archivo=archivo)
            insert.save()
            return render(request,"registros/archivos.html")
        else:
            messages.error(request, "Error al procesar el formulario")

    else:
        return render(request,"registros/archivos.html",{'archivo':Archivos})
    
def consultasSQL(request):
    alumnos = Alumnos.objects.raw(
        'SELECT id, matricula, nombre, carrera, turno, imagen '
        'FROM registros_alumnos '
        'WHERE carrera = "TI" '
        'ORDER BY turno DESC'
    )

    return render(request, "registros/consultas.html", {'alumnos': alumnos})
