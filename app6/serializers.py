from rest_framework import serializers
from .models import Comentario

class ComentarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id_comentario','articulo','usuario','contenido','fecha_creacion','activo','comentario_padre']