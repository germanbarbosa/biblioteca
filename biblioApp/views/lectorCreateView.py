from django.db.models.query import QuerySet
from django.views import generic
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,RetrieveUpdateAPIView
from biblioApp.models.lector import Lector


from biblioApp.serializers.lectorSerializer import LectorSerializer

class LectorListApiView(ListAPIView):
    serializer_class = LectorSerializer
    
    def get_queryset(self):
        return Lector.objects.all()
    
class LectorCreateView(CreateAPIView):
    serializer_class = LectorSerializer
    
    def get_queryset(self):
        return Lector.objects.all()
    
class LectorDetailView(RetrieveAPIView):
    serializer_class =LectorSerializer
    
    def get_queryset(self):
        #return Autor.objects.all()
        return Lector.objects.filter(anulate=False)
    
class LectorDeleteView(DestroyAPIView):
    serializer_class = LectorSerializer
    
    queryset = Lector.objects.all()
    

class LectorUpdateView(UpdateAPIView):
    serializer_class = LectorSerializer
    
    queryset = Lector.objects.all()

class LectorRetriveUpdateView(RetrieveUpdateAPIView):
    serializer_class = LectorSerializer
    
    def get_queryset(self):
        return Lector.objects.all()