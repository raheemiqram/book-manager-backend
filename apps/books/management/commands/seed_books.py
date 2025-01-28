import random
from django.core.management.base import BaseCommand

from apps.books.models import BookList, Book


class Command(BaseCommand):
    help = "Seed the database with test data for Book and BookList models"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding test data...")

        BookList.objects.all().delete()
        Book.objects.all().delete()

        books = []
        for i in range(1, 101):
            book = Book(
                title=f"Book Title {i}",
                year=random.randint(1900, 2025),
                author=f"Author {i}"
            )
            books.append(book)

        Book.objects.bulk_create(books)
        self.stdout.write(f"Created {len(books)} books.")

        all_books = Book.objects.all()

        for i in range(1, 11):
            book_list = BookList.objects.create(name=f"Book List {i}")
            book_list.books.set(random.sample(list(all_books), k=random.randint(10, 20)))
            self.stdout.write(f"Created Book List {book_list.name} with {book_list.books.count()} books.")

        self.stdout.write(self.style.SUCCESS("Test data successfully seeded!"))
