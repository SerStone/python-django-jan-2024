from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.dataclasses.user_dataclass import UserDataClass
from core.services.email_service import EmailService
from core.services.jwt_service import ActivateFToken, ActivateToken, JWTService

from apps.users.models import UserModel
from apps.users.serializer import UserForgetPassSerializer, UserSerializer


class UserActivateView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        token = kwargs['token']
        user: UserModel = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserRestorePassView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        token = kwargs['token']
        if not token:
            return Response({"detail": "Token not provided"}, status=status.HTTP_400_BAD_REQUEST)

        user: UserModel = JWTService.validate_token(token, ActivateFToken)
        if not user:
            return Response({"detail": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)

        new_password = request.data.get('new_password')
        if not new_password:
            return Response({"detail": "New password not provided"}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()

        return Response({"detail": "Password reset successfully"}, status=status.HTTP_200_OK)


class ForgetPassView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserForgetPassSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        user = get_object_or_404(UserModel, email=email)
        EmailService.forgot_password(user)

        return Response({"detail": "Password reset email sent successfully"}, status=status.HTTP_200_OK)
