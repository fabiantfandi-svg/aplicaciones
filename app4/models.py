from django.db import models

class Revisor(models.Model):
    id_revisor = models.AutoField(primary_key=True)
    usuario = models.OneToOneField("app1.Usuario",on_delete=models.CASCADE)
    area_expertise = models.CharField(max_length=200)
    max_articulos = models.IntegerField(default=5)
    disponible = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 