from Empleado.models import Empleado
from rest_framework import serializers
from Empleado.api.serializers.general_serializers import CargoSerializer, DepartamentoSerializer


class EmpleadosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empleado
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
