from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from base.api import GeneralListApiView
from Empleado.api.serializers.general_serializers import DepartamentoSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    serializer_class = DepartamentoSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
    
    def list(self, request):
        departamento_serializer=self.get_serializer(self.get_queryset(), many=True)
        return Response(departamento_serializer.data,status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Cargo creado correctamente!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            departamento_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)

            if departamento_serializer.is_valid():
                departamento_serializer.save()
                return Response({'message':'Departamento ha sido modificado correctamente!'}, status=status.HTTP_200_OK)
            return Response(departamento_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        departamento = self.get_queryset().filter(id=pk).first()
        if departamento:
            departamento.state = False
            departamento.save()
            return Response({'message': 'Departamento Eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un departamento con esos datos'}, status=status.HTTP_400_BAD_REQUEST)

