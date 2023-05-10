from Empleado.models import Departamento,Cargo

from rest_framework import serializers 



class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        exclude=('state','created_date','modified_date','deleted_date')

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        exclude=('state','created_date','modified_date','deleted_date')