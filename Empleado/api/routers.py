from rest_framework.routers import DefaultRouter
from django.urls import path
from Empleado.api.views.empleados_viewsets import *
from Empleado.api.views.cargos_viewsets import *
from Empleado.api.views.departamento_viewsets import *
from Empleado.api.views.incapacidad_viewsets import *
from Empleado.api.views.renta_viewsets import *
from Empleado.api.views.prestaciones_viewsets import *
from Empleado.api.views.ausencia_viewsets import *
from Empleado.api.views.indemnizacion_viewsets import *
router = DefaultRouter()



router.register(r'empleados', EmpleadosViewSet, basename='empleados')
router.register(r'cargo', CargoViewSet, basename='cargo')
router.register(r'departamento', DepartamentoViewSet, basename='departamento')
router.register(r'incapacidad', IncapacidadesViewSet, basename='incapacidad')
#router.register(r'renta', RentaViewSet, basename='incapacidad')
router.register(r'prestaciones',PrestacionesViewSet, basename='prestacion')
router.register(r'ausencia',AusenciaViewSet, basename='ausencia')
router.register(r'indemnizacion',IndemnizacionesViewSet, basename='indemnizacion')
urlpatterns = router.urls


