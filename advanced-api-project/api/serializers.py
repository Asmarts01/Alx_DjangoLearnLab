from rest_framework import serializers
from .models import Book, Author

# Serializer for Book model

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

# Nested serializer to include author's books

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
    
    def validate(self, data):
        if 'title' in data and len(data['title']) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return data