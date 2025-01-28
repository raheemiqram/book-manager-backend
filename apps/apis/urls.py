from django.urls import path

from apps.apis.views.book_views import BookListView, BookListCreateView, BookListUpdateDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('book-lists/', BookListCreateView.as_view(), name='book-list-create'),
    path('book-lists/<int:pk>/', BookListUpdateDeleteView.as_view(), name='book-list-detail'),
]