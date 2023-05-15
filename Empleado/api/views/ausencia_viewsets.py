from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from base.api import GeneralListApiView
from Empleado.api.serializers.general_serializers import AusenciaSerializer

class AusenciaViewSet(viewsets.ModelViewSet):
    serializer_class = AusenciaSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
    
    def list(self, request):
        Ausencia_serializer=self.get_serializer(self.get_queryset(), many=True)
        return Response(Ausencia_serializer.data,status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Ausencia creado correctamente!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            Ausencia_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)

            if Ausencia_serializer.is_valid():
                Ausencia_serializer.save()
                return Response({'message':'Ausencia ha sido modificada correctamente!'}, status=status.HTTP_200_OK)
            return Response(Ausencia_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        Ausencia = self.get_queryset().filter(id=pk).first()
        if Ausencia:
            Ausencia.state = False
            Ausencia.save()
            return Response({'message': 'Ausencia Eliminada correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe una Ausencia con esos datos'}, status=status.HTTP_400_BAD_REQUEST)

