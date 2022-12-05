from rest_framework import serializers

from applications.product.models import Books


class BooksSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Books
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user

        book = Books.objects.create(owner=user, **validated_data)
        return book
