from rest_framework import viewsets, filters, serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'genre', 'author__name']

    def perform_create(self, serializer):
        if serializer.validated_data['category'] == 'textbook':
            existing_books = Book.objects.filter(
                title=serializer.validated_data['title'],
                year=serializer.validated_data['year'],
                publisher=serializer.validated_data['publisher'],
                category='textbook',
            )
            if existing_books.exists():
                raise serializers.ValidationError('Учебник уже существует в этом издании')
        serializer.save()
