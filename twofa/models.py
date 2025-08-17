from django.db import models

class User2FA(models.Model):
    email = models.EmailField(unique=True)
    secret = models.CharField(max_length=32)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.email

# Modelo de prueba para verificar migraciones y creación de tabla
from django.db import models

class User2FA(models.Model):
    email = models.EmailField(unique=True)
    secret = models.CharField(max_length=32)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.email