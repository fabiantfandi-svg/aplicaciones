from rest_framework import serializers
from .models import Etiqueta

class EtiquetaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = ['id_etiqueta','nombre','descripcion','fecha_creacion']