from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'price', 'year', 'created_at', 'updated_at')

    def validate_brand(self, value):
        if value == 'LARA':
            raise ValidationError({'details': 'brand == LARA'})
        return value
