from rest_framework import serializers

from bbbs.books.models import Book, Tag

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug')

        
class BookSerializer(serializers.ModelSerializer):
    tag = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Book
        exclude = ("show_on_main_page",)
