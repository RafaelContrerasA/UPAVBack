from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import User
from .serializers import UserRegisterSerializer, UserUpdateSerializer, UserSerializer
from django.contrib.auth import update_session_auth_hash
from .serializers import ChangePasswordSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from django.core.cache import cache

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class RegisterView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                'rol': openapi.Schema(type=openapi.TYPE_INTEGER),
            },
            required=['username', 'email', 'password']  # Especifica los campos requeridos en el payload
        )
    )
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'message': 'Usuario registrado exitosamente.',
                'user': UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)



class UserView(APIView):
    


    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request):
        user = request.user
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)  # Indicar que se permite actualización parcial
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            # Verificar si la contraseña anterior es correcta
            if not user.check_password(serializer.validated_data['old_password']):
                return Response({'old_password': ['La contraseña anterior es incorrecta.']}, status=status.HTTP_400_BAD_REQUEST)
            # Verificar si la nueva contraseña y la confirmación coinciden
            if serializer.validated_data['new_password'] != serializer.validated_data['confirm_new_password']:
                return Response({'confirm_new_password': ['Las contraseñas nuevas no coinciden.']}, status=status.HTTP_400_BAD_REQUEST)
            # Cambiar la contraseña
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            # Actualizar la sesión de autenticación
            update_session_auth_hash(request, user)
            return Response({'message': 'Contraseña cambiada correctamente.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        cache_key = f"login_attempts_{email}"
        attempts = cache.get(cache_key, 0)
        tiempo_bloqueo = 300


        if attempts >= 5:
            return Response({'error': 'Demasiados intentos, intentelo mas tarde.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            response = super().post(request, *args, **kwargs)

            print("codigo response")
            print(response.status_code)

            if response.status_code == status.HTTP_401_UNAUTHORIZED:
                cache.set(cache_key, attempts + 1, timeout=tiempo_bloqueo)  # Tiempo total de bloqueo en segundos

            return response

        except Exception as e:
            print(f"Exception occurred: {e}")
            cache.set(cache_key, attempts + 1, timeout=tiempo_bloqueo)
            return Response({'error': 'Error, intentelo de nuevo.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDeleteView(APIView):

    def delete(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
            user.delete()
            return Response({'message': 'Usuario eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'error': 'El usuario no existe.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': 'Hubo un error al eliminar el usuario.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)