from biblioApp.models.libro import Categoria
from rest_framework import fields, serializers

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombre']