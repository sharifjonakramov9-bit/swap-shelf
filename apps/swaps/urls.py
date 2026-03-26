from django.urls import path
from .views import (
    SwapRequestCreateView,
    IncomingSwapListView,
    OutgoingSwapListView,
    SwapRequestAcceptView,
    SwapRequestRejectView
)

urlpatterns = [
    path("requests/", SwapRequestCreateView.as_view(), name="swap-request-create"),
    path("requests/incoming/", IncomingSwapListView.as_view(), name="swap-incoming"),
    path("requests/outgoing/", OutgoingSwapListView.as_view(), name="swap-outgoing"),
    path("requests/<int:pk>/accept/", SwapRequestAcceptView.as_view(), name="swap-accept"),
    path("requests/<int:pk>/reject/", SwapRequestRejectView.as_view(), name="swap-reject"),
]