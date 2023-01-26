from django.urls import path
from .views import PurchasedPolicyListView, PurchasedPolicyDetailView

urlpatterns = [
    path('', PurchasedPolicyListView.as_view()),
    path('<int:pk>/', PurchasedPolicyDetailView.as_view()),
]
