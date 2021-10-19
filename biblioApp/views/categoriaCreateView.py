from django.db.models.query import QuerySet
from django.views import generic
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,RetrieveUpdateAPIView
from biblioApp.models.libro import Categoria

from biblioApp.serializers.categoriaSeralizer import CategoriaSerializer

class CategoriaListApiView(ListAPIView):
    serializer_class = CategoriaSerializer
    
    def get_queryset(self):
        return Categoria.objects.all()
    
class CategoriaCreateView(CreateAPIView):
    serializer_class = CategoriaSerializer
    
    def get_queryset(self):
        return Categoria.objects.all()
    
class CategoriaDetailView(RetrieveAPIView):
    serializer_class =CategoriaSerializer
    
    def get_queryset(self):
        #return Autor.objects.all()
        return Categoria.objects.filter(anulate=False)
    
class CategoriaDeleteView(DestroyAPIView):
    serializer_class = CategoriaSerializer
    
    queryset = Categoria.objects.all()
    

class CategoriaUpdateView(UpdateAPIView):
    serializer_class = CategoriaSerializer
    
    queryset = Categoria.objects.all()

class CategoriaRetriveUpdateView(RetrieveUpdateAPIView):
    serializer_class = CategoriaSerializer
    
    def get_queryset(self):
        return Categoria.objects.all()