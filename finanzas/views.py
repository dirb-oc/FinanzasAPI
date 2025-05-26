# views.py
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from .serializers import *
from datetime import datetime

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

class IngresoRangoFechaAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        fecha_inicio_param = request.data.get('fecha_inicio')
        fecha_fin_param = request.data.get('fecha_fin')

        if not fecha_inicio_param or not fecha_fin_param:
            return Response({"message": "Se requieren las fechas de inicio y fin."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            fecha_inicio = datetime.strptime(fecha_inicio_param, "%Y-%m-%d").date()
            fecha_fin = datetime.strptime(fecha_fin_param, "%Y-%m-%d").date()

            ingresos = Ingreso.objects.filter(
                usuario=request.user,
                activo=True,
                fecha__range=[fecha_inicio, fecha_fin]
            )

            serializer = IngresoSerializer(ingresos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except ValueError as e:
            return Response({"message": "El formato de fecha es inválido. Use 'YYYY-MM-DD'.", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class GastoViewSet(BaseUserQuerySetViewSet):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer

class GastoRangoFechaAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        fecha_inicio_param = request.data.get('fecha_inicio')
        fecha_fin_param = request.data.get('fecha_fin')

        if not fecha_inicio_param or not fecha_fin_param:
            return Response({"message": "Se requieren las fechas de inicio y fin."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            fecha_inicio = datetime.strptime(fecha_inicio_param, "%Y-%m-%d").date()
            fecha_fin = datetime.strptime(fecha_fin_param, "%Y-%m-%d").date()

            gastos = Gasto.objects.filter(
                usuario=request.user,
                activo=True,
                fecha__range=[fecha_inicio, fecha_fin]
            )

            serializer = GastoSerializer(gastos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except ValueError:
            return Response({"message": "El formato de las fechas es incorrecto. Use 'YYYY-MM-DD'."}, status=status.HTTP_400_BAD_REQUEST)

class AhorroViewSet(BaseUserQuerySetViewSet):
    queryset = Ahorro.objects.all()
    serializer_class = AhorroSerializer

class GastoFijoViewSet(BaseUserQuerySetViewSet):
    queryset = GastoFijo.objects.all()
    serializer_class = GastoFijoSerializer

class ObjetivoViewSet(BaseUserQuerySetViewSet):
    queryset = ObjetivosFinancieros.objects.all()
    serializer_class = ObjetivoSerializer
