from django.urls import path

from AppRegistros.views import inicio, servicios

urlpatterns = [
    path('', inicio, name='AppRegistrosInicio'),
    path('servicios/', servicios, name='AppRegistrosServicios'),
]