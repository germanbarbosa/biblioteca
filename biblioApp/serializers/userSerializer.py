from rest_framework import serializers
from biblioApp.models.user import User
from biblioApp.models.lector import Lector
from biblioApp.serializers.lectorSerializer import LectorSerializer

class UserSerializer(serializers.ModelSerializer):
    lector = LectorSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'lector']
        
        
    def create(self, validated_data):
        lectorData = validated_data.pop('lector')
        userInstance = User.objects.create(**validated_data)
        Lector.objects.create(user=userInstance, **lectorData)
        return userInstance
    
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        lector = Lector.objects.get(user=obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'email': user.email,
            'lector': {
                'nombre': lector.nombre,
                'apellidos': lector.apellidos,
                'nacionalidad': lector.nacionalidad,
                'edad': lector.edad
                }
            }
