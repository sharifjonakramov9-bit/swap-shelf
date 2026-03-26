from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError, PermissionDenied
from .models import SwapRequest, Swap, SwapRequestStatus
from .serializers import SwapRequestSerializer, SwapSerializer
from apps.books.models import Book, BookStatus

# ➕ SwapRequest yaratish
class SwapRequestCreateView(generics.CreateAPIView):
    queryset = SwapRequest.objects.all()
    serializer_class = SwapRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        book = serializer.validated_data["book"]

        if book.owner == self.request.user:
            raise ValidationError("You cannot request your own book")

        if book.status != BookStatus.AVAILABLE:
            raise ValidationError("Book is not available")

        if SwapRequest.objects.filter(
            from_user=self.request.user,
            book=book,
            status=SwapRequestStatus.PENDING
        ).exists():
            raise ValidationError("You already requested this book")

        serializer.save(
            from_user=self.request.user,
            to_user=book.owner
        )

# ➕ Incoming swap requests (to me)
class IncomingSwapListView(generics.ListAPIView):
    serializer_class = SwapRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SwapRequest.objects.filter(to_user=self.request.user)

# ➕ Outgoing swap requests (from me)
class OutgoingSwapListView(generics.ListAPIView):
    serializer_class = SwapRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SwapRequest.objects.filter(from_user=self.request.user)

# ✅ Accept swap request
class SwapRequestAcceptView(generics.UpdateAPIView):
    queryset = SwapRequest.objects.all()
    serializer_class = SwapRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        swap_request = self.get_object()

        if swap_request.to_user != self.request.user:
            raise PermissionDenied("Not allowed")

        serializer.save(status=SwapRequestStatus.ACCEPTED)

        # Book status update
        swap_request.book.status = BookStatus.UNAVAILABLE
        swap_request.book.save()

        # Create Swap
        Swap.objects.create(
            book=swap_request.book,
            owner=swap_request.to_user,
            borrower=swap_request.from_user,
            type=swap_request.book.type
        )

# ❌ Reject swap request
class SwapRequestRejectView(generics.UpdateAPIView):
    queryset = SwapRequest.objects.all()
    serializer_class = SwapRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        swap_request = self.get_object()
        if swap_request.to_user != self.request.user:
            raise PermissionDenied("Not allowed")
        serializer.save(status=SwapRequestStatus.REJECTED)