from Empleado.models import Departamento, Cargo, Incapacidad, Retencion, Prestaciones, Ausencia, Indemnizacion

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
            "departamento": instance.departamento,
            "id_empleado": f'{instance.id_empleado.nombres} {instance.id_empleado.apellidos}'
        }


class RentaSerializar(serializers.ModelSerializer):
    class Meta:
        model = Retencion
        fields = '__all__'


class PrestacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestaciones
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "departamento": instance.departamento,
            "salario": instance.salario,
            "isss_laboral": instance.isss_laboral,
            "isss_patronal": instance.isss_patronal,
            "afp_laboral": instance.afp_laboral,
            "afp_patronal": instance.afp_patronal,
            "impuesto_renta": instance.impuesto_renta,
            "total_descuento": instance.total_descuento,
            "sueldo_liquido": instance.sueldo_liquido,
            "empleado": f'{instance.empleado.nombres} {instance.empleado.apellidos}'
        }


class AusenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ausencia
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "cantidad_dias": instance.cantidad_dias,
            "fecha_inicio": instance.fecha_inicio,
            "fecha_final": instance.fecha_final,
            "departamento": instance.departamento,
            "id_empleado": f'{instance.id_empleado.nombres} {instance.id_empleado.apellidos}'
        }


class IndemnizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indemnizacion
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "dias": instance.dias,
            "pago": instance.pago,
            "años_completos": instance.años_completos,
            "salario": instance.salario,
            "fecha_ingreso": instance.fecha_ingreso,
            "fecha_retiro": instance.fecha_retiro,
            "departamento": instance.departamento,
            "empleado": f'{instance.empleado.nombres} {instance.empleado.apellidos}'
        }
