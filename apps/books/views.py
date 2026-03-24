from rest_framework import viewsets

from apps.books.models import Book
from apps.books.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    