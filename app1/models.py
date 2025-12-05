from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    TIPO_USUARIO =[
        ('estudiante','Estudiante'),
        ('profesor','Profesor'),
        ('investigador','Investigador'),
        ('admin','Administrador'),
    ]
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO)
    institucion = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    especialidad = models.CharField(max_length=100, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return 