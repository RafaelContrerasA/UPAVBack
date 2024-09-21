from rest_framework.viewsets import ModelViewSet
from apis.models import Rol, Tipo, Dependencia, Publicacion, Logs, Image, Video
from apis.api.serializers import RolSerializer, TipoSerializer, DependenciaSerializer, PublicacionSerializer, LogsSerializer, ImageSerializer, VideoSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class RolApiViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated]
    
    serializer_class = RolSerializer
    queryset = Rol.objects.all()

class TipoApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TipoSerializer
    queryset = Tipo.objects.all()

class DependenciaApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = DependenciaSerializer
    queryset = Dependencia.objects.all()

class PublicacionApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PublicacionSerializer
    queryset = Publicacion.objects.all()

class LogsApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LogsSerializer
    queryset = Logs.objects.all()

class ImageApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

class VideoApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = VideoSerializer
    queryset = Video.objects.all()