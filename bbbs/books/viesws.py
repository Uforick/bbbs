from rest_framework import generics

from bbbs.books.models import Book, Tag
from bbbs.books.serializers import BookSerializer, TagSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookTagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None