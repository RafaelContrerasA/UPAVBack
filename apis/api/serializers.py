from rest_framework import serializers
from apis.models import Rol, Tipo, Dependencia, Publicacion, Logs, Image, Video

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id','nombre']
        
class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ['id','nombre']

class DependenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependencia
        fields = ['id','nombre','pagina_fb','pertenece_a','tipo','status','siglas']

class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = ['id','link','time','text','id_dependencia','me_gusta','me_encanta','me_divierte','me_asombra',
                  'me_entristece','me_enoja','me_importa']
        
class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = ['id','accion','fecha'] 

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id','url','extracted_text','id_publicacion']

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id','url','video_thumbnail','id_publicacion']