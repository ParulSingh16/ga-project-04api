from django.urls import path
from .views import CustomerRegisteration

urlpatterns = [
    path('', CustomerRegisteration.as_view()),
    path('create/', CustomerRegisteration.add_items, name='add-items'),
    path('all/', CustomerRegisteration.view_items, name='view_items'),
]
