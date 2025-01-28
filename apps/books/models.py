from django.db import models
from apps.core.models import BaseModel


class Book(BaseModel):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class BookList(BaseModel):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="lists")

    def __str__(self):
        return self.name
