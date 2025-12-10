from rest_framework import serializers
from .models import ArticuloEtiqueta

class ArticuloEtiquetaSerializers(serializers.ModelSerializer):
    class Meta:
        model = ArticuloEtiqueta
        fields = ['id_articuloetiqueta','articulo','etiqueta','fecha_asignacion']