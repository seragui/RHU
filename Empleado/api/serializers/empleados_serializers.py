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
                "flag_discapacidad": instance.flag_discapacidad,
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


""""
"id": 1,
        "nombres": "Ronald Antonio",
        "apellidos": "Sermeño Aguilar",
        "fecha_nacimiento": "1997-08-21",
        "direccion": "Ejemplo",
        "telefono": "50370895605",
        "sexo": "M",
        "flag_discapacidad": false,
        "documento_identidad": "05597691-3",
        "correo": "rasa0821@hotmail.com",
        "estado_civil": "soltero",
        "no_isss": "012345678",
        "no_afp": "012345678512",
        "salario": "1500.00",
        "fecha_contratacion": "2023-05-12",
        "tipo_pago": "Mensual",
        "tipo_contrato": "Formal",
        "cargo": 1,
        "id_departamento": 1
"""