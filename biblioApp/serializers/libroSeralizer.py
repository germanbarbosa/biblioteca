from biblioApp.models.libro import Libro
from rest_framework import fields, serializers

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['titulo','categoria','autores','fecha_lanzamiento','portada','visitas']