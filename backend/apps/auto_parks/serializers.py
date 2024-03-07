from rest_framework import serializers

from apps.auto_parks.models import AutoParkModel

# from apps.cars.serializers import CarSerializer
# from apps.users.models import ProfileModel

# class AutoParkSerializer(serializers.ModelSerializer):
#     cars = CarSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = AutoParkModel
#         fields = ('id', 'name', 'created_at', 'updated_at')


class AutoParkWithOutCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'created_at', 'updated_at')
