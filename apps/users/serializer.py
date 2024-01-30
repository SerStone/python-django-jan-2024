from rest_framework import serializers

from apps.auto_parks.serializers import AutoParkWithOutCarsSerializer
from apps.users.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    auto_parks = AutoParkWithOutCarsSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'age', 'gender', 'updated_at', 'created_at', 'auto_parks')
