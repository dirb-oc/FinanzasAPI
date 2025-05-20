from rest_framework import serializers
from .models import *

class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingreso
        fields = ['id', 'cantidad', 'fecha']
        read_only_fields = ['usuario', 'activo']

class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = ['id','descripcion','cantidad','fecha']
        read_only_fields = ['usuario', 'activo']


class AhorroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ahorro
        fields = ['id', 'cantidad', 'fecha','nombre', 'fecha_Final']
        read_only_fields = ['id', 'fecha']

class GastoFijoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GastoFijo
        fields = ['id', 'cantidad','frecuencia']
        read_only_fields = ['id', 'fecha']

class FrecuenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frecuencia
        fields = '__all__'