from django.db import models
from apps.users.models import User
from apps.books.models import Book
from apps.books.choices import BookType, BookStatus

class SwapRequestStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    ACCEPTED = "accepted", "Accepted"
    REJECTED = "rejected", "Rejected"

class SwapRequest(models.Model):
    book = models.ForeignKey(Book, related_name="swap_requests", on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, related_name="sent_swap_requests", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="received_swap_requests", on_delete=models.CASCADE)
    message = models.CharField(max_length=500, blank=True)
    status = models.CharField(max_length=10, choices=SwapRequestStatus.choices, default=SwapRequestStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

class SwapStatus(models.TextChoices):
    ACTIVE = "active", "Active"
    COMPLETED = "completed", "Completed"
    CANCELLED = "cancelled", "Cancelled"

class Swap(models.Model):
    book = models.ForeignKey(Book, related_name="swaps", on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name="owned_swaps", on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, related_name="borrowed_swaps", on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=BookType.choices)  # ✅ BookType import qilingan
    status = models.CharField(max_length=10, choices=SwapStatus.choices, default=SwapStatus.ACTIVE)
    return_deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)