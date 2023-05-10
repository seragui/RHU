from django.http import JsonResponse
from django.shortcuts import render
from Empleado.models import Empleado

# Create your views here.
def ver_empleado(request, empleado_id):
    try:
        empleado = Empleado.objects.get(id=empleado_id)
        salario = empleado.salario

        # Realizar los cálculos de descuentos
        afp = float(salario) * 0.1  # Descuento del 10% para AFP
        isss = float(salario) * 0.03  # Descuento del 3% para ISSS

        descuentos = {
            'AFP': afp,
            'ISSS': isss
        }

        data = {
        'empleado': {
            'id': empleado.id,
            'nombres': empleado.nombres,
            'apellidos': empleado.apellidos,
            # Agrega más campos del empleado según sea necesario
        },
        'salario': float(salario),
        'descuentos': descuentos
    }

        return JsonResponse(data)
    except Empleado.DoesNotExist:
        return JsonResponse({'error': 'Empleado no encontrado'}, status=404)