from django.db import models

class Biblioteca(models.Model):
    TIPO_RECURSO = [
        ('libro','Libro'),
        ('paper','Paper Cientifico'),
        ('tesis','Tesis'),
        ('video','Video'),
        ('')
    ]