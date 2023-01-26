from django.urls import path
from .views import PolicyDetailView, PolicyListView

urlpatterns = [
    path('', PolicyListView.as_view()),
    path('<str:name>/', PolicyDetailView.as_view()),
]
