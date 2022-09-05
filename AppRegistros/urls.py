from django.urls import path

from AppRegistros.views import inicio, servicios, portafolio, registros, equipo, contactos

urlpatterns = [
    path('', inicio, name='AppRegistrosInicio'),
    path('servicios/', servicios, name='AppRegistrosServicios'),
    path('portafolio/', portafolio, name='AppRegistrosPortafolio'),
    path('registros/', registros, name='AppRegistrosRegistros'),
    path('equipo/', equipo, name='AppRegistrosEquipo'),
    path('contactos/', contactos, name='AppRegistrosContactos'),
]