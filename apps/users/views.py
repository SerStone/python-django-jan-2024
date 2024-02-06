from rest_framework.generics import CreateAPIView

from apps.users.serializer import UserSerializer


class UserCreateApiView(CreateAPIView):
    serializer_class = UserSerializer

