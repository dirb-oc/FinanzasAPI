from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'ingresos', IngresoViewSet, basename='ingreso')
router.register(r'gastos', GastoViewSet, basename='gasto')
router.register(r'ahorros', AhorroViewSet)
router.register(r'gastosfijos', GastoFijoViewSet)
router.register(r'frecuencia', FrecuenciaSetViewSet)
router.register(r'objetivo', ObjetivoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('I_rango/', IngresoRangoFechaAPIView.as_view(), name='ingresos-rango'),
    path('G_rango/', GastoRangoFechaAPIView.as_view(), name='gasto-rango'),
]