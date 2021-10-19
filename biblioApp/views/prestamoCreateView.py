from django.db.models.query import QuerySet
from django.views import generic
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,RetrieveUpdateAPIView
from biblioApp.models.lector import Prestamo

from biblioApp.serializers.prestamoSerializer import PrestamoSerializer

class PrestamoListApiView(ListAPIView):
    serializer_class = PrestamoSerializer
    
    def get_queryset(self):
        return Prestamo.objects.all()
    
class PrestamoCreateView(CreateAPIView):
    serializer_class = PrestamoSerializer
    
    def get_queryset(self):
        return Prestamo.objects.all()
    
class PrestamoDetailView(RetrieveAPIView):
    serializer_class = PrestamoSerializer
    
    def get_queryset(self):
        #return Autor.objects.all()
        return Prestamo.objects.filter(anulate=False)
    
class PrestamoDeleteView(DestroyAPIView):
    serializer_class = PrestamoSerializer
    
    queryset = Prestamo.objects.all()
    

class PrestamoUpdateView(UpdateAPIView):
    serializer_class = PrestamoSerializer
    
    queryset = Prestamo.objects.all()

class PrestamoRetriveUpdateView(RetrieveUpdateAPIView):
    serializer_class = PrestamoSerializer
    
    def get_queryset(self):
        return Prestamo.objects.all()