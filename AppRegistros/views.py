from django.shortcuts import render

def inicio(request):

    return render(request, 'index.html')

def servicios(request):

    return render(request, 'AppBody/servicios.html')

def portafolio(request):

    return render(request, 'AppBody/portafolio.html')

def registros(request):

    return render(request, 'AppBody/registros.html')

def equipo(request):

    return render(request, 'AppBody/equipo.html')

def contactos(request):

    return render(request, 'AppBody/contactos.html')