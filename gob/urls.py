"""
URL configuration for gob project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apis.api.router import router_rol, router_tipo, router_dependencia, router_publicacion 
from apis.api.router import router_logs, router_image, router_video
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="Documentación de la API del UPAV",
      terms_of_service="",
      contact=openapi.Contact(email="gibranca123@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   # permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_rol.urls)),
    path('api/', include(router_tipo.urls)),
    path('api/', include(router_dependencia.urls)),
    path('api/', include(router_publicacion.urls)),
    path('api/', include(router_logs.urls)),
    path('api/', include(router_image.urls)),
    path('api/', include(router_video.urls)),
    path('api/', include('users.api.router')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

