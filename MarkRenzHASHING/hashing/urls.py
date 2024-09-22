from django.urls import path
from .views import hash_view

urlpatterns = [
    path('hash/', hash_view, name='hash_view'),
]
