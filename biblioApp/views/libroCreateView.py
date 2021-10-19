from django.db.models.query import QuerySet
from django.views import generic
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,RetrieveUpdateAPIView
from biblioApp.models.libro import Libro

from biblioApp.serializers.libroSeralizer import LibroSerializer

class LibroListApiView(ListAPIView):
    serializer_class = LibroSerializer
    
    def get_queryset(self):
        return Libro.objects.all()
    
class LibroCreateView(CreateAPIView):
    serializer_class = LibroSerializer
    
    def get_queryset(self):
        return Libro.objects.all()
    
class LibroDetailView(RetrieveAPIView):
    serializer_class = LibroSerializer
    
    def get_queryset(self):
        #return Autor.objects.all()
        return Libro.objects.filter(anulate=False)
    
class LibroDeleteView(DestroyAPIView):
    serializer_class = LibroSerializer
    
    queryset = Libro.objects.all()
    

class LibroUpdateView(UpdateAPIView):
    serializer_class = LibroSerializer
    
    queryset = Libro.objects.all()

class LibroRetriveUpdateView(RetrieveUpdateAPIView):
    serializer_class = LibroSerializer
    
    def get_queryset(self):
        return Libro.objects.all()