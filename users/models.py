from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    rol = models.ForeignKey('apis.Rol', on_delete=models.CASCADE, default=5)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Solicitar el nombre de usuario al crear un usuario desde la consola de administración
   

    def __str__(self):
        return self.username
