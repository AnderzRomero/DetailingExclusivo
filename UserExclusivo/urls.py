from django.contrib.auth.views import LogoutView
from django.urls import path, include

from UserExclusivo.views import *

urlpatterns =[
    path('login/', login_request, name='UserExclusivoLogin'),
    path('registro/', register, name='UserExclusivoRegister'),
    path('logout/', LogoutView.as_view(template_name='UserExclusivo/logout.html'), name='UserExclusivoLogout'),
    path('editar/', editar_usuario, name='UserExclusivoEditar'),
    path('avatar/', upload_avatar, name='UserExclusivoAvatar'),
]