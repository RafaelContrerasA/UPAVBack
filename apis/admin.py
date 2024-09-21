from django.contrib import admin

from apis.models import Tipo, Dependencia, Publicacion, Rol, Logs, Image, Video

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre']

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display=['id','nombre']

@admin.register(Dependencia)
class DependenciaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','pagina_fb', 'pertenece_a','tipo','status','siglas']

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ['id','link','time','text','id_dependencia','me_gusta','me_encanta',
                    'me_divierte','me_asombra','me_entristece','me_enoja','me_importa']
@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ['id','accion','fecha']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','url','extracted_text']

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id','url','video_thumbnail','id_publicacion' ]    