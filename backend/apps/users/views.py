from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from core.permissions.is_admin_or_write_only_permission import IsAdminOrWriteOnlyPermission
from core.permissions.is_superuser import IsSuperuser

from apps.users.models import ProfileModel
from apps.users.serializer import ProfileAvatarSerializer, UserSerializer

from .models import UserModel as User

UserModel = get_user_model()


@method_decorator(name='get', decorator=swagger_auto_schema(security=[]))
class UserCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsAdminOrWriteOnlyPermission,)


class MeView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserAddAvatarView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileAvatarSerializer
    http_method_names = ('put',)

    def get_object(self):
        return self.request.user.profile

    def perform_update(self, serializer):
        profile: ProfileModel = self.get_object()
        profile.avatar.delete()
        super().perform_update(serializer)


class UserToAdminView(GenericAPIView):
    permission_classes = (IsSuperuser,)

    def get_serializer(self):
        pass

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def put(self, *args, **kwargs):
        user: User = self.get_object()

        if not user.is_staff:
            user.is_staff = True
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class AdminToUserView(GenericAPIView):
    permission_classes = (IsSuperuser,)

    def get_serializer(self):
        pass

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def put(self, *args, **kwargs):
        user: User = self.get_object()

        if user.is_staff:
            user.is_staff = False
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserBlockView(GenericAPIView):
    permission_classes = (IsAdminUser,)

    def get_serializer(self):
        pass

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def put(self, *args, **kwargs):
        user: User = self.get_object()

        if user.is_active:
            user.is_active = False
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserUnblockView(GenericAPIView):
    permission_classes = (IsAdminUser,)

    def get_serializer(self):
        pass

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    @swagger_auto_schema(security=[])
    def put(self, *args, **kwargs):
        user: User = self.get_object()

        if not user.is_active:
            user.is_active = True
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)
