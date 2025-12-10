from rest_framework import serializers
from .models import Favorito

class FavoritoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = ['id_favorito','usuario','articulo','fecha_agregado']