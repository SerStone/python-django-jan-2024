from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'price', 'year', 'body_type', 'created_at', 'updated_at', 'car_photo')


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('car_photo',)
        extra_kwargs = {
            'car_photo': {
                'required': True
            }
        }

    def validate_brand(self, value):
        if value == 'LARA':
            raise ValidationError({'details': 'brand == LARA'})
        return value
