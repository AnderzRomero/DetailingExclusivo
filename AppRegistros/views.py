from django.shortcuts import render, redirect

from AppRegistros.forms import ClientesFormulario, BusquedaNombreFormulario
from AppRegistros.models import Clientes


def busqueda_nombre_post(request):
    nombre = request.GET.get('nombre')

    clientes = Clientes.objects.all()
    contexto = {
        'clientes': clientes
    }

    return render(request, 'AppBody/cliente_filtrado.html', contexto)


def busqueda_nombre(request):
    contexto = {
        'form': BusquedaNombreFormulario(),
    }

    return render(request, 'AppBody/busquedanombre.html', contexto)


def registros(request):
    if request.method == 'POST':

        mi_formulario = ClientesFormulario(request.POST)

        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data

            cliente1 = Clientes(nombre=data.get('nombre'), apellidos=data.get('apellidos'),
                                telefono=data.get('telefono'), email=data.get('email'))
            cliente1.save()

            return redirect('AppRegistrosRegistros')

    clientes = Clientes.objects.all()

    contexto = {
        'form': ClientesFormulario(),
        'clientes': clientes
    }

    return render(request, 'AppBody/registros.html', contexto)


def inicio(request):
    return render(request, 'index.html')


def servicios(request):
    return render(request, 'AppBody/servicios.html')


def portafolio(request):
    return render(request, 'AppBody/portafolio.html')


def equipo(request):
    return render(request, 'AppBody/equipo.html')
