from django.db import models


class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

class Tipo(models.Model):
    id  = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

class Dependencia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    pagina_fb = models.URLField()
    pertenece_a = models.ForeignKey('self', on_delete= models.CASCADE, null=True, blank=True)
    tipo = models.ForeignKey(Tipo, on_delete = models.CASCADE)
    status = models.CharField(max_length=10)
    siglas = models.CharField(max_length=10)

class Publicacion(models.Model):
    id = models.AutoField(primary_key=True)
    link = models.URLField()
    time = models.DateTimeField()
    text = models.CharField(max_length=200)
    id_dependencia = models.ForeignKey(Dependencia, on_delete=models.CASCADE)
    me_gusta = models.IntegerField()
    me_encanta = models.IntegerField()
    me_divierte = models.IntegerField()
    me_asombra = models.IntegerField()
    me_entristece = models.IntegerField()
    me_enoja = models.IntegerField()
    me_importa = models.IntegerField()

from users.models import User
class Logs(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, on_delete= models.CASCADE, default=1) 
    accion = models.CharField(max_length=50)
    fecha = models.DateTimeField()



class Image(models.Model):
    id = models.AutoField(primary_key= True)
    url = models.URLField()
    extracted_text = models.CharField(max_length=50)
    id_publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)


class Video(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField()
    video_thumbnail = models.CharField(max_length=100)
    id_publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)


