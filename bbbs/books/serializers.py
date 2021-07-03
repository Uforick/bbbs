from rest_framework import serializers

from bbbs.books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ("show_on_main_page",)
