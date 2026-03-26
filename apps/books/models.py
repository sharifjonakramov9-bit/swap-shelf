from django.db import models
from apps.users.models import User
from .choices import BookCondition, BookType, BookStatus

class Genre(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    owner = models.ForeignKey(User, related_name="books", on_delete=models.CASCADE)
    title = models.CharField(max_length=124)
    author = models.CharField(max_length=64)
    genre = models.ForeignKey(Genre, related_name="books", on_delete=models.PROTECT)
    condition = models.CharField(
        max_length=16, choices=BookCondition.choices, default=BookCondition.GOOD
    )
    type = models.CharField(
        max_length=16, choices=BookType.choices, default=BookType.BORROW
    )
    description = models.CharField(max_length=999, blank=False)
    image = models.URLField()
    status = models.CharField(
        max_length=16, choices=BookStatus.choices, default=BookStatus.AVAILABLE
    )
    image = models.URLField(blank=True, null=True)
    status = models.CharField(choices=BookStatus.choices, default=BookStatus.AVAILABLE)
    share = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} - {self.author}"
    created_at = models.DateTimeField(auto_now_add=True)
