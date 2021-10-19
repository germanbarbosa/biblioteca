from biblioApp.models.autor import Autor
from rest_framework import fields, serializers

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['nombre','apellidos','nacionalidad','edad']