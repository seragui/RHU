from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from base.api import GeneralListApiView
from Empleado.api.serializers.general_serializers import CargoSerializer

class CargoViewSet(viewsets.ModelViewSet):
    serializer_class = CargoSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
    
    def list(self, request):
        cargo_serializer=self.get_serializer(self.get_queryset(), many=True)
        return Response(cargo_serializer.data,status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Cargo creado correctamente!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            cargo_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)

            if cargo_serializer.is_valid():
                cargo_serializer.save()
                return Response({'message':'Cargo ha sido modificado correctamente!'}, status=status.HTTP_200_OK)
            return Response(cargo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        cargo = self.get_queryset().filter(id=pk).first()
        if cargo:
            cargo.state = False
            cargo.save()
            return Response({'message': 'Cargo Eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un cargo con esos datos'}, status=status.HTTP_400_BAD_REQUEST)

