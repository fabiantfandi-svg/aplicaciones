from rest_framework import serializers
from .models import Biblioteca

class BibliotecaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Biblioteca
        fields = ['id_biblioteca','titulo','autor','tipo_recurso','archivo','descripcion','fecha_subida','subido_por','publico']