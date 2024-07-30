from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import BookModel
from .serializers import BookSerializers


# class BookListApiView(generics.ListAPIView):
    
#     queryset = BookModel.objects.all()
#     serializer_class = BookSerializers
    

class BookListApiView(APIView):
    
    def get(self, request):
        book_list = BookModel.objects.all()
        serializer_data = BookSerializers(book_list, many=True).data
        
        data = {
            'number_of_books' : len(book_list),
            'book_list' : serializer_data,
        }
        
        return Response(data=data)
    
    
@api_view(['GET',])
def book_list_api_view(request, *args, **kwargs):
    book_list = BookModel.objects.all()
    serializer = BookSerializers(book_list, many=True)
    return Response(serializer.data)


# class BookDetailApiView(generics.RetrieveAPIView):
    
#     queryset = BookModel.objects.all()
#     serializer_class = BookSerializers
    
    
class BookDetailApiView(APIView):
    
    def get(self, request, pk):
        book_list = BookModel.objects.get(id=pk)
        serializer_data = BookSerializers(book_list).data
        
        data = {
            "serializer_data" : serializer_data,
        }
        
        return Response(data)
    
    
class BookDeteleApiView(generics.DestroyAPIView):
    
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers
    

# class BookUpdateApiView(generics.UpdateAPIView):
    
#     queryset = BookModel.objects.all()
#     serializer_class = BookSerializers


class BookUpdateApiView(APIView):
    
    def put(self, request, pk):
            book = get_object_or_404(BookModel.objects.all(), id=pk)
            data = request.data
            book_serializer = BookSerializers(instance=book, data=data, partial=True)
            if book_serializer.is_valid(raise_exception=True):
                book_saved = book_serializer.save()
    
            return Response({'status':True,
                             'message':f'{book_saved}'})
    
    
# class BookCreateApiView(generics.CreateAPIView):
    
#     queryset = BookModel.objects.all()
#     serializer_class = BookSerializers


class BookCreateApiView(APIView):
    
    def post(self, request):
        data = request.data
        serializer_list = BookSerializers(data=data)
        if serializer_list.is_valid():
            serializer_list.save()
        
            data = {
                'serializer_list' : data
            }
            return Response(data=data)
        

class BookListCreateApiView(generics.ListCreateAPIView):
    
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers
    
    
class BookDetailUpdateApiView(generics.RetrieveUpdateAPIView):
    
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers
    
    
class BookDetailDestroyApiView(generics.RetrieveDestroyAPIView):
    
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers


class BookDetailUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers
    
        