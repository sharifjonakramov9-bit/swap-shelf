from rest_framework import serializers

from .models import Book, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class BookListSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True)
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            "id",
            "owner",
            "title",
            "author",
            "genre",
            "condition",
            "type",
            "description",
            "image",
            "status",
            "share",
            "created_at",
        ]

    def get_owner(self, obj):
        return {
            "id": obj.owner_id,
            "name": obj.owner.name,
            "telegram_id": obj.owner.telegram_id,
            "telegram_username": obj.owner.telegram_username,
        }


class BookWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "genre",
            "condition",
            "type",
            "description",
            "image",
            "status",
            "share",
        ]

    def create(self, validated_data):
        return Book.objects.create(owner=self.context["request"].user, **validated_data)
