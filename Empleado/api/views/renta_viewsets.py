from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from base.api import GeneralListApiView
from Empleado.api.serializers.general_serializers import RentaSerializar

class RentaViewSet(viewsets.ModelViewSet):
    serializer_class = RentaSerializar

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter()
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk).first()
    
    def list(self, request):
        Renta_serializer=self.get_serializer(self.get_queryset(), many=True)
        return Response(Renta_serializer.data,status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Tramo creado correctamente!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            Renta_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)

            if Renta_serializer.is_valid():
                Renta_serializer.save()
                return Response({'message':'Tramo ha sido modificada correctamente!'}, status=status.HTTP_200_OK)
            return Response(Renta_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        Renta = self.get_queryset().filter(id=pk).first()
        if Renta:
            Renta.state = False
            Renta.save()
            return Response({'message': 'Tramo Eliminada correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe una Incapacidad con esos datos'}, status=status.HTTP_400_BAD_REQUEST)

