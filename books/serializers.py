from django_filters.utils import verbose_field_name
from rest_framework import serializers

from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(
        label='Автор',
        queryset=Author.objects.all(),
        source='author',
        write_only=True
    )
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
