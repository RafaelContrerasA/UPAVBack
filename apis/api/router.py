from rest_framework.routers import DefaultRouter
from apis.api.views import RolApiViewSet, TipoApiViewSet, DependenciaApiViewSet
from apis.api.views import PublicacionApiViewSet, LogsApiViewSet, ImageApiViewSet, VideoApiViewSet

router_rol = DefaultRouter()
router_rol.register(prefix='rol', basename = 'rol', viewset = RolApiViewSet )

router_tipo = DefaultRouter()
router_tipo.register(prefix='tipo', basename = 'tipo', viewset = TipoApiViewSet )

router_dependencia = DefaultRouter()
router_dependencia.register(prefix='dependencia', basename = 'dependencia', viewset = DependenciaApiViewSet )

router_publicacion = DefaultRouter()
router_publicacion.register(prefix='publicacion', basename = 'publicacion', viewset = PublicacionApiViewSet )

router_logs = DefaultRouter()
router_logs.register(prefix='logs', basename = 'logs', viewset = LogsApiViewSet )

router_image = DefaultRouter()
router_image.register(prefix='image', basename = 'image', viewset = ImageApiViewSet )

router_video = DefaultRouter()
router_video.register(prefix='video', basename = 'video', viewset = VideoApiViewSet )