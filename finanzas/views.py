# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class FrecuenciaSetViewSet(viewsets.ModelViewSet):
    queryset = Frecuencia.objects.all()
    serializer_class = FrecuenciaSerializer

class BaseUserQuerySetViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(usuario=self.request.user, activo=True)

    def perform_destroy(self, instance):
        instance.activo = False
        instance.save()

class IngresoViewSet(BaseUserQuerySetViewSet):
    queryset = Ingreso.objects.all()
    serializer_class = IngresoSerializer

class GastoViewSet(BaseUserQuerySetViewSet):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer

class AhorroViewSet(BaseUserQuerySetViewSet):
    queryset = Ahorro.objects.all()
    serializer_class = AhorroSerializer

class GastoFijoViewSet(BaseUserQuerySetViewSet):
    queryset = GastoFijo.objects.all()
    serializer_class = GastoFijoSerializer
