from django.db import models

class Articulo(models.Model):
    id_articulo = models.AutoField(primary_key=True)
    ESTADO_ARTICULO = [
        ('borrador','Borrador'),
        ('revision','En Revision'),
        ('publicado','Publicado'),
        ('rechazado','Rechazado'),
    ]
    titulo = models.CharField(max_length=200)
    resumen = models.TextField()
    contenido = models.TextField()
    autor = models.ForeignKey("app1.Usuario",on_delete=models.CASCADE)
    categoria = models.ForeignKey("app2.Categoria",on_delete=models.SET_NULL,null=True)
    estado = models.CharField(max_length=200,choices=ESTADO_ARTICULO,default="borrador")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_publicacion = models.DateTimeField(null=True,blank=True)
    palabras_clave = models.CharField(max_length=200)
    visitas = models.IntegerField(default=0)
    def __str__(self):
        return 