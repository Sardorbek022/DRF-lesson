from rest_framework import generics

from .models import BookModel
from .serializers import BookSerializers


class BookListApiView(generics.ListAPIView):
    
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers