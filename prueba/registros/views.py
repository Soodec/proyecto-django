from django.shortcuts import render
from .forms import ComentarioContactoForm
from .models import ComentarioContacto
from django.shortcuts import get_object_or_404

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
    
    
    