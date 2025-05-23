from rest_framework import serializers
from .models import *

class IngresoSerializer(serializers.ModelSerializer):
    cantidad = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)
    class Meta:
        model = Ingreso
        fields = ['id', 'cantidad', 'fecha']
        read_only_fields = ['id','usuario', 'activo']

class GastoSerializer(serializers.ModelSerializer):
    cantidad = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)
    class Meta:
        model = Gasto
        fields = ['id','descripcion','cantidad','fecha']
        read_only_fields = ['id','usuario', 'activo']

class AhorroSerializer(serializers.ModelSerializer):
    cantidad = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)
    class Meta:
        model = Ahorro
        fields = ['id', 'cantidad', 'fecha','nombre', 'fecha_Final']
        read_only_fields = ['id','usuario', 'activo']

class GastoFijoSerializer(serializers.ModelSerializer):
    cantidad = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)
    class Meta:
        model = GastoFijo
        fields = ['id', 'cantidad','frecuencia']
        read_only_fields = ['id', 'fecha','activo']

class FrecuenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frecuencia
        fields = '__all__'

class ObjetivoSerializer(serializers.ModelSerializer):
    meta = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)
    actual = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)
    class Meta:
        model = ObjetivosFinancieros 
        fields = ['id', 'descripcion','meta','actual']
        read_only_fields = ['id', 'usuario','activo']