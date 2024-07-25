from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import BookModel
from .serializers import BookSerializers


class BookListApiView(generics.ListAPIView):
    
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers
    
    
@api_view(['GET',])
def book_list_api_view(request, *args, **kwargs):
    book_list = BookModel.objects.all()
    serializer = BookSerializers(book_list, many=True)
    return Response(serializer.data)


class BookDetailApiView(generics.RetrieveAPIView):
    
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers
    
    
class BookDeteleApiView(generics.DestroyAPIView):
    
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers
    

class BookUpdateApiView(generics.UpdateAPIView):
    
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers
    
    
        