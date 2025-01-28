from rest_framework import serializers

from apps.books.models import Book, BookList


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), many=True)  # Accept a list of book IDs

    class Meta:
        model = BookList
        fields = ['id', 'name', 'books']

    def to_representation(self, instance):
        # Overriding to_representation to return book objects in the response
        representation = super().to_representation(instance)
        book_ids = representation.get('books', [])

        # Use the BookSerializer to serialize the book objects
        book_serializer = BookSerializer(Book.objects.filter(id__in=book_ids), many=True)
        representation['books'] = book_serializer.data
        return representation
