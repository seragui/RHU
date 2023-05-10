from rest_framework.routers import DefaultRouter
from django.urls import path
from Empleado.api.views.empleados_viewsets import *
from Empleado.api.views.cargos_viewsets import *
from Empleado.api.views.departamento_viewsets import *
router = DefaultRouter()

router.register(r'empleados', EmpleadosViewSet, basename='empleados')
router.register(r'cargo', CargoViewSet, basename='cargo')
router.register(r'departamento', DepartamentoViewSet, basename='departamento')
urlpatterns = router.urls

