from django.urls import path
from Empleado.views import *

"""Asignacion de la rutas de la aplicacion
"""

urlpatterns = [
    # ... otras rutas de la aplicación ...
    #
    path('empleados/<int:empleado_id>/', ver_empleado, name='ver_empleado'),
]