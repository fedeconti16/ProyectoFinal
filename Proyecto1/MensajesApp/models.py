from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='mensajes/', blank=True, null=True)

    def __str__(self):
        return self.content
