from rest_framework import serializers

from book.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=True, read_only=True, slug_field="username")

    class Meta:
        model = Book
        fields = ("id", "title", "author")


class BookDetailSerializer(BookSerializer):
    author = serializers.SlugRelatedField(many=True, read_only=True, slug_field="username")

    class Meta:
        model = Book
        fields = ("id", "title", "author", "description")
