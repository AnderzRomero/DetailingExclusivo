import http
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

from UserExclusivo.forms import UserRegisterForm, AvatarForm
from UserExclusivo.models import Avatar


def upload_avatar(request):
    if request.method == "POST":

        formulario = AvatarForm(request.POST, request.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data
            avatar = Avatar.objects.filter(user=data.get("usuario"))

            if len(avatar) > 0:
                 avatar = avatar[0]
                 avatar.imagen = formulario.changed_data["imagen"]
                 avatar.save()

            else:
                 avatar = Avatar(user=data.get("user"), imagen=data.get("imagen"))
                 avatar.save()

        return redirect("AppRegistrosInicio")

    contexto = {
        "form": AvatarForm(),
        'boton_envio': 'Crear'
    }
    return render(request, "base_formularios.html", contexto)


@login_required
def editar_usuario(request):
    usuario = request.user
    if request.method == 'POST':

        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data
            usuario.username = data.get('username')
            usuario.email = data.get('email')
            usuario.last_name = data.get('first_name')
            usuario.last_name = data.get('last_name')

            usuario.save()

            messages.info(request, 'Tu usuario fue resgristrado satisfactoriamente!')
        else:
            messages.info(request, 'Tu usuario no pudo ser registrado!')
        return redirect('AppRegistrosInicio')
    contexto = {
        'form': UserRegisterForm(
            initial={'username': usuario.username,
                     'email': usuario.email,
                     'first_name': usuario.first_name,
                     'last_name': usuario.last_name
                     }),
        'boton_envio': 'Registro',
    }

    return render(request, 'base_formularios.html', contexto)

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)
                messages.info(request, 'Inicio de sesion satisfactorio!')


            else:
                messages.info(request, 'Porfavor verificar usuario o contraseña!')

        else:
            messages.info(request, 'Inicio de sesion fallido!')

        return  redirect('AppRegistrosInicio')



    contexto = {
        'form': AuthenticationForm(),
        'titulo_form': 'Login',
        'boton_envio': 'Enviar'
    }
    return render(request, 'base_formularios.html', contexto)

def register(request):
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()

            messages.info(request, 'Tu usuario fue resgristrado satisfactoriamente!')
        else:
            messages.info(request, 'Tu usuario no pudo ser registrado!')
        return redirect('AppRegistrosInicio')

    contexto = {
        'form': UserRegisterForm(),
        'titulo_form': 'Registro',
        'boton_envio': 'Registro'
    }

    return render(request, 'base_formularios.html', contexto)