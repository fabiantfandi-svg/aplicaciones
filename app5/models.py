from django.db import models

class Revision(models.Model):
    id_revision = models.AutoField(primary_key=True)
    articulo = models.ForeignKey("app3.Articulo",on_delete=models.CASCADE)
    revisor = models.ForeignKey("app4.Revisor",on_delete=models.CASCADE)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    fecha_completa = models.DateTimeField(null=True, blank=True)
    comentarios = models.TextField()
    calificacion = models.IntegerField(choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')])
    recomendacion = models.CharField(max_length=50, choices=[
        ('aceptar','Aceptar'),
        ('aceptar_con_modificaciones','Aceptar con Modificaciones'),
        ('rechazar','Rechazar')
    ])
    def __str__(self):
        return 
