from rest_framework import generics

from apps.apis.serializers.book_serializers import BookSerializer, BookListSerializer
from apps.books.models import Book, BookList

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all().order_by('-created_at')
    serializer_class = BookSerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = BookList.objects.all().order_by('-created_at')
    serializer_class = BookListSerializer


class BookListUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookList.objects.all().order_by('-created_at')
    serializer_class = BookListSerializer
