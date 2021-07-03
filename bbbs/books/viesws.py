from rest_framework import generics

from bbbs.books.models import Book
from bbbs.books.serializers import BookSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
