from django.urls import path

from .views import BookListApiView


urlpatterns = [
    path('book-list/', view=BookListApiView.as_view(), ),
]
