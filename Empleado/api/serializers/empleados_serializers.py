from Empleado.models import Empleado
from rest_framework import serializers
from Empleado.api.serializers.general_serializers import CargoSerializer, DepartamentoSerializer


class EmpleadosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empleado
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    def to_representation(self, instance):
            return{
                'id': instance.id,
                'nombres': instance.nombres,
                'apellidos': instance.apellidos,
                'fecha_nacimiento': instance.fecha_nacimiento,
                'direccion': instance.direccion,
                'telefono': instance.telefono,
                'sexo': instance.sexo,
                "documento_identidad": instance.documento_identidad,
                "correo": instance.correo,
                "estado_civil": instance.estado_civil,
                "no_isss": instance.no_isss,
                "no_afp": instance.no_afp,
                "salario": instance.salario,
                "fecha_contratacion": instance.fecha_contratacion,
                "tipo_contrato": instance.tipo_contrato,
                "cargo": instance.cargo.nombre_cargo,
                "id_departamento":  instance.id_departamento.nombre_departamento

            }


