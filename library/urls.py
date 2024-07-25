from django.urls import path

from .views import (BookListApiView, book_list_api_view, BookDetailApiView, 
        BookDeteleApiView, BookUpdateApiView, BookCreateApiView,
        BookListCreateApiView, BookDetailUpdateApiView, BookDetailDestroyApiView, BookDetailUpdateDeleteApiView, 
    )


urlpatterns = [
    path('book-list/', view=BookListApiView.as_view(), ),
    path('book-create/', view=BookCreateApiView.as_view(), ),
    path('book-list-create/', view=BookListCreateApiView.as_view(), ),
    path('book/<int:pk>/', view=BookDetailApiView.as_view(), ),
    path('book/<int:pk>/delete/', view=BookDetailDestroyApiView.as_view(), ),
    path('book/<int:pk>/update/', view=BookDetailUpdateApiView.as_view(), ),
    path('book/<int:pk>/update/delete/', view=BookDetailUpdateDeleteApiView.as_view(), ),
    path('book-delete/<int:pk>/', view=BookDeteleApiView.as_view(), ),
    path('book-update/<int:pk>/', view=BookUpdateApiView.as_view(), ),
    path('book-list1/', view=book_list_api_view, ),
]
