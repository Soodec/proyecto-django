from django.shortcuts import render, HttpResponse

# Menú simple (opcional)

def principal(request):
    # Renderiza un template. Asegúrate de crear este archivo (ver abajo).
    # Si prefieres, puedes pasar el menú en el contexto.
    return render(request, "inicio/principal.html")

def contacto(request):
    
    return render(request, "inicio/contacto.html")

def registrar(request):
    
    return render(request, "inicio/formulario.html")

def ejemplo(request):
    return render (request, "inicio/ejemplo.html")
