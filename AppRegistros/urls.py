from django.urls import path

from AppRegistros.views import inicio, servicios, portafolio, registros, equipo, busqueda_nombre, busqueda_nombre_post

urlpatterns = [
    path('', inicio, name='AppRegistrosInicio'),
    path('servicios/', servicios, name='AppRegistrosServicios'),
    path('portafolio/', portafolio, name='AppRegistrosPortafolio'),
    path('registros/', registros, name='AppRegistrosRegistros'),
    path('equipo/', equipo, name='AppRegistrosEquipo'),
    path('busqueda_nombre/', busqueda_nombre, name='AppRegistrosBusquedaNombre'),
    path('busqueda_nombre_post/', busqueda_nombre_post, name='AppRegistrosBusquedaNombrePost'),

]