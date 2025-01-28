from rest_framework import serializers

from apps.books.models import Book, BookList


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = BookList
        fields = ['id', 'name', 'books']
