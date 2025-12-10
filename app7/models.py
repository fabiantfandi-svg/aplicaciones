from django.db import models

class Favorito(models.Model):
    id_favorito = models.AutoField(primary_key=True)
    usuario = models.ForeignKey("app1.Usuario",on_delete=models.CASCADE)
    articulo = models.ForeignKey("app3.Articulo",on_delete=models.CASCADE)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 