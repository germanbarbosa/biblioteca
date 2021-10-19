from biblioApp.models.lector import Prestamo
from rest_framework import fields, serializers

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = ['lector','libro','fecha_prestamo','fecha_devolucion','devuelto']