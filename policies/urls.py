from django.urls import path
from .views import PolicyListView

urlpatterns = [
    path('', PolicyListView.as_view()),
]
