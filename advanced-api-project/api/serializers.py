from rest_framework import serializers
from .models import Book, Author
from datetime import timezone

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year']
    
    def validate(self, date):
        if date > timezone.now().year:
            raise serializers.ValidationError('The publication year can not be in the future')

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

#model.py
#Author: represent an author with a one-to-many relationship to books
#Book: represent a book with a title and a publication_year and a foreign key to the author

#serializers.py
#BookSerializer
#AuthorSerializer