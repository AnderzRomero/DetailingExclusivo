from django.shortcuts import render

def inicio(request):

    return render(request, 'index.html')

def servicios(request):

    return render(request, 'AppBody/servicios.html')
