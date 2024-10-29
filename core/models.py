from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.username  # Muestra el nombre de usuario en la interfaz de administración

class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)  # Agrega una fecha de creación para el comentario

    def __str__(self):
        return f'Comentario de {self.usuario.username}: {self.contenido[:20]}'  # Muestra el inicio del contenido del comentario
