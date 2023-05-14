from Empleado.models import Departamento, Cargo, Incapacidad, Retencion

from rest_framework import serializers


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class IncapacidadSerializar(serializers.ModelSerializer):
    class Meta:
        model = Incapacidad
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "cantidad_dias": instance.cantidad_dias,
            "motivo": instance.motivo,
            "fecha_inicio": instance.fecha_inicio,
            "fecha_final": instance.fecha_final,
            "documentacion": instance.documentacion,
            "id_empleado": f'{instance.id_empleado.nombres} {instance.id_empleado.apellidos}'
        }
    
class RentaSerializar(serializers.ModelSerializer):
    class Meta:
        model= Retencion
        fields='__all__'
