from django.db import models

class Comentario(models.Model):
        id_comentario = models.AutoField(primary_key=True)
        articulo = models.ForeignKey("app3.Articulo",on_delete=models.CASCADE)
        usuario = models.ForeignKey("app1.Usuario",on_delete=models.CASCADE)
        contenido = models.TextField()
        fecha_creacion = models.DateTimeField(auto_now_add=True)
        activo = models.BooleanField(default=True)
        comentario_padre = models.ForeignKey("self",on_delete=models.CASCADE ,null=True,blank=True)
        def __str__(self):
                return 