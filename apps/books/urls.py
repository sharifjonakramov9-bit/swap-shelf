from django.urls import path
from apps.books.views import (
    BookDetailView,
    BookListCreateView,
    GenreDetailView,
    GenreListCreateView,
)

urlpatterns = [
    path("genres/", GenreListCreateView.as_view(), name="genre-list-create"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
    path("books/", BookListCreateView.as_view(), name="book-list-create"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
]
