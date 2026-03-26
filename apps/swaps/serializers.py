from rest_framework import serializers
from .models import SwapRequest, Swap
from apps.books.models import Book
from apps.books.serializers import BookSerializer
from apps.users.serializers import UserSerializer

class SwapRequestSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(),  # <<<< queryset kerak
        source="book",
        write_only=True
    )
    from_user = UserSerializer(read_only=True)
    to_user = UserSerializer(read_only=True)

    class Meta:
        model = SwapRequest
        fields = "__all__"

class SwapSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    owner = UserSerializer(read_only=True)
    borrower = UserSerializer(read_only=True)

    class Meta:
        model = Swap
        fields = "__all__"