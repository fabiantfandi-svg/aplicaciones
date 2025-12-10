from django.db import models

class Biblioteca(models.Model):
    id_biblioteca = models.AutoField(primary_key=True)
    TIPO_RECURSO = [
        ('libro','Libro'),
        ('paper','Paper Cientifico'),
        ('tesis','Tesis'),
        ('video','Video'),
        ('presentacion','Presentacion')
    ]
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    tipo_recurso = models.CharField(max_length=20,choices=TIPO_RECURSO)
    archivo = models.FileField(upload_to="bibloteca/")
    descripcion = models.TextField()
    fecha_subida = models.DateTimeField(auto_now_add=True)
    subido_por = models.ForeignKey("app1.Usuario",on_delete=models.CASCADE)
    publico = models.BooleanField(default=True)
    def __str__(self):
        return 