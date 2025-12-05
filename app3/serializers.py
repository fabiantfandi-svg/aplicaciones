from rest_framework import serializers
from .models import Articulo

class ArticuloSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ['id_articulo','titulo','resumen','contenido','autor','categoria','estado','fecha_creacion','fecha_publicacion','palabras_clave','visitas']