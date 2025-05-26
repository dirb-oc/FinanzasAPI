from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', '')
        )
        return user

class CambiarPasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        usuario = request.user
        password_actual = request.data.get('password_actual')
        nueva_password = request.data.get('nueva_password')

        if not password_actual or not nueva_password:
            return Response({'error': 'Se requieren los campos password_actual y nueva_password.'},
                            status=status.HTTP_400_BAD_REQUEST)

        if not usuario.check_password(password_actual):
            return Response({'error': 'La contraseña actual es incorrecta.'},
                            status=status.HTTP_403_FORBIDDEN)

        usuario.set_password(nueva_password)
        usuario.save()

        return Response({'mensaje': 'Contraseña actualizada correctamente.'}, status=status.HTTP_200_OK)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
