from django.urls import path
from .views import list_books, book_detail

urlpatterns = [
    path('list_books/', list_books, name='list_books'),
    path('book_detail/<int:id>/', book_detail, name='book_detail'),
]