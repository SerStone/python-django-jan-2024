from rest_framework import serializers

from .models import CarModel


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=20)
    year = serializers.IntegerField()


class CarListSerializer(CarSerializer):
    pass


class CarSerializer(CarListSerializer):
    cabin_type = serializers.CharField(max_length=20)
    count_of_saddles = serializers.IntegerField()
    engine_type = serializers.FloatField()
    price = serializers.IntegerField()

    def create(self, validated_data):
        car = CarModel.objects.create(**validated_data)
        return car

    def update(self, instance, validated_data: dict):
        for k, v in validated_data.items():
            setattr(instance, k, v)

        instance.save()
        return instance