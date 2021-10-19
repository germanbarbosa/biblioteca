from django.db.models.query import QuerySet
from django.views import generic
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,RetrieveUpdateAPIView
from biblioApp.models.autor import Autor

from biblioApp.serializers.autorSerializer import AutorSerializer

class AutorListApiView(ListAPIView):
    serializer_class = AutorSerializer
    
    def get_queryset(self):
        return Autor.objects.all()
    
class AutorCreateView(CreateAPIView):
    serializer_class = AutorSerializer
    
    def get_queryset(self):
        return Autor.objects.all()
    
class AutorDetailView(RetrieveAPIView):
    serializer_class = AutorSerializer
    
    def get_queryset(self):
        #return Autor.objects.all()
        return Autor.objects.filter(anulate=False)
    
class AutorDeleteView(DestroyAPIView):
    serializer_class = AutorSerializer
    
    queryset = Autor.objects.all()
    

class AutorUpdateView(UpdateAPIView):
    serializer_class = AutorSerializer
    
    queryset = Autor.objects.all()

class AutorRetriveUpdateView(RetrieveUpdateAPIView):
    serializer_class = AutorSerializer
    
    def get_queryset(self):
        return Autor.objects.all()
    
