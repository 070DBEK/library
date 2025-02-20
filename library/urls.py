from django.urls import path
from .views import BookListCreateView, BookDetailView


app_name = 'library'


urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]