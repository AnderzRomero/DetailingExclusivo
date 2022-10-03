from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('', lambda req: redirect('AppRegistrosInicio')),
    path('admin/', admin.site.urls),
    path('AppRegistros/', include('AppRegistros.urls')),
    path('UserExclusivo/', include('UserExclusivo.urls'))
]

