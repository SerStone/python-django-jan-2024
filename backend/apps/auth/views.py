from django.contrib.auth import get_user_model
from django.views.generic import detail

from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.dataclasses.user_dataclass import UserDataClass
from core.services.email_service import EmailService
from core.services.jwt_service import ActivateFToken, ActivateToken, JWTService, SocketToken

from apps.auth.serializers import EmailSerializer, PasswordSerializers
from apps.users.models import UserModel as User
from apps.users.serializer import UserSerializer

UserModel = get_user_model()


class UserActivateView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        token = kwargs['token']
        user: UserModel = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class ForgetPassView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = EmailSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        user = get_object_or_404(UserModel, email=email)
        EmailService.forgot_password(user)

        return Response({"detail": "Password reset email sent successfully"}, status=status.HTTP_200_OK)


class UserRestorePassView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PasswordSerializers

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        token = kwargs['token']
        user: User = JWTService.validate_token(token, ActivateFToken)
        user.set_password(serializer.data['password'])
        user.save()
        return Response({detail: "Password reset successful"}, status=status.HTTP_200_OK)


class SocketView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        token = JWTService.create_token(self.request.user, SocketToken)
        return Response({"token": str(token)}, status=status.HTTP_200_OK)
