from django.urls import path
from Usuario.views import *

"""Asignacion de la rutas de la aplicacion
"""

urlpatterns = [
    path('crear_usuario/', RegistrarUsuario.as_view(), name='crear_usuario'),
]
