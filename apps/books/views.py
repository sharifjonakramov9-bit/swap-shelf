from rest_framework import generics, permissions

from .models import Book, Genre
from .serializers import BookListSerializer, BookWriteSerializer, GenreSerializer


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner_id == request.user.id


class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.order_by("name")
    serializer_class = GenreSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.select_related("owner", "genre").all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return BookListSerializer
        return BookWriteSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        queryset = super().get_queryset()
        genre_id = self.request.query_params.get("genre")
        owner_id = self.request.query_params.get("owner")
        status_value = self.request.query_params.get("status")

        if genre_id:
            queryset = queryset.filter(genre_id=genre_id)
        if owner_id:
            queryset = queryset.filter(owner_id=owner_id)
        if status_value:
            queryset = queryset.filter(status=status_value)
        return queryset


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.select_related("owner", "genre").all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return BookListSerializer
        return BookWriteSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]
