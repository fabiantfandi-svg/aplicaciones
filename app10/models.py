from django.db import models

class ArticuloEtiqueta(models.Model):
    id_articuloetiqueta = models.AutoField(primary_key=True)
    articulo = models.ForeignKey("app3.Articulo",on_delete=models.CASCADE)
    etiqueta = models.ForeignKey("app9.Etiqueta",on_delete=models.CASCADE)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 