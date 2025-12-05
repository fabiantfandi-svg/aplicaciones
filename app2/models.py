from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    color = models.CharField(max_length=7,default='#007bff')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 