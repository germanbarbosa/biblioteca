from django.db import models
from biblioApp.models.lector import Lector
from rest_framework import fields, serializers

class LectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lector
        fields = ['user','nombre','apellidos','nacionalidad','edad']