from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from base.api import GeneralListApiView
from Empleado.api.serializers.general_serializers import IncapacidadSerializar

class IncapacidadesViewSet(viewsets.ModelViewSet):
    serializer_class = IncapacidadSerializar

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
    
    def list(self, request):
        Incapacidades_serializer=self.get_serializer(self.get_queryset(), many=True)
        return Response(Incapacidades_serializer.data,status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Incapacidad creado correctamente!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            Incapacidades_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)

            if Incapacidades_serializer.is_valid():
                Incapacidades_serializer.save()
                return Response({'message':'Incapacidad ha sido modificada correctamente!'}, status=status.HTTP_200_OK)
            return Response(Incapacidades_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        Incapacidades = self.get_queryset().filter(id=pk).first()
        if Incapacidades:
            Incapacidades.state = False
            Incapacidades.save()
            return Response({'message': 'Incapacidad Eliminada correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe una Incapacidad con esos datos'}, status=status.HTTP_400_BAD_REQUEST)

