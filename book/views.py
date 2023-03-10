from rest_framework import viewsets

from book.models import Book
from book.serializers import (
    BookSerializer,
    BookListSerializer,
    BookDetailSerializer,
)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.prefetch_related("author")
    serializer_class = BookSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return BookListSerializer
        if self.action == "retrieve":
            return BookDetailSerializer
        return BookSerializer
