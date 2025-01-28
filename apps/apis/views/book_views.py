from rest_framework import generics

from apps.apis.serializers.book_serializers import BookSerializer, BookListSerializer
from apps.books.models import Book, BookList


# List all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Manage book lists
class BookListCreateView(generics.ListCreateAPIView):
    queryset = BookList.objects.all()
    serializer_class = BookListSerializer


class BookListUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookList.objects.all()
    serializer_class = BookListSerializer
