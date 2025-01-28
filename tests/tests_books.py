from rest_framework.test import APITestCase
from rest_framework import status
from apps.books.models import Book, BookList
from django.urls import reverse

class BookListViewsTestCase(APITestCase):

    def setUp(self):
        # Create test books
        self.book1 = Book.objects.create(title='Book 1', author='Author 1', year=2025)
        self.book2 = Book.objects.create(title='Book 2', author='Author 2',year=2024)

        # Create test book lists
        self.book_list = BookList.objects.create(name='Test List')

        self.book_list.books.add(self.book1)
        self.book_list.books.add(self.book2)

        # URLs
        self.book_list_url = reverse('book-list')  # URL for the BookListView
        self.book_list_create_url = reverse('book-list-create')  # URL for the BookListCreateView
        self.book_list_detail_url = reverse('book-list-detail', args=[self.book_list.id])  # URL for the BookListUpdateDeleteView

    def test_get_book_list(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)  # Check if the list returns 2 books
        self.assertEqual(response.data['results'][0]['title'], 'Book 1')
        self.assertEqual(response.data['results'][1]['title'], 'Book 2')

    def test_create_book_list(self):
        data = {'name': 'New Book List', 'books': [self.book1.id]}
        response = self.client.post(self.book_list_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'New Book List')
        self.assertEqual(response.data['books'][0]['id'], self.book1.id)

    def test_update_book_list(self):
        updated_data = {'name': 'Updated Book List'}
        response = self.client.patch(self.book_list_detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Book List')

    def test_delete_book_list(self):
        response = self.client.delete(self.book_list_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



    def test_create_book_list_invalid_data(self):
        data = {'name': ''}  # Empty name field
        response = self.client.post(self.book_list_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

