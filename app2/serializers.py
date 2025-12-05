from rest_framework import serializers
from .models import Categoria

class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id_categoria','nombre','descripcion','color','fecha_creacion']