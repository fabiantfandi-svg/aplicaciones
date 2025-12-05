from rest_framework import serializers
from .models import Usuario

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario','nombre','email','tipo_usuario','institucion','fecha_registro','especialidad','activo']