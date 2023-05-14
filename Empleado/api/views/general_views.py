from base.api import GeneralListApiView

from Empleado.models import Cargo, Departamento
from Empleado.api.serializers.general_serializers import CargoSerializer, DepartamentoSerializer, IncapacidadSerializar, RentaSerializar

class CargoAPIView(GeneralListApiView):
    serializer_class= CargoSerializer

class DepartamentoAPIView(GeneralListApiView):
    serializer_class= DepartamentoSerializer

class IncapacidadAPIView(GeneralListApiView):
    serializer_class= IncapacidadSerializar

class RentaAPIView(GeneralListApiView):
    serializer_class=RentaSerializar