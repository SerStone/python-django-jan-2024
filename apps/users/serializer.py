from rest_framework import serializers

from apps.auto_parks.serializers import AutoParkSerializer
from apps.users.models import UserModel


class UserAutoParkSerializer(AutoParkSerializer):
    class Meta(AutoParkSerializer.Meta):
        fields = ('id', 'user', 'name', 'created_at', 'updated_at')


class UserSerializer(serializers.ModelSerializer):
    auto_parks = UserAutoParkSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'age', 'gender', 'created_at', 'updated_at', 'auto_parks')