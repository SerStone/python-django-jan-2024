from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.auth.views import ForgetPassView, UserActivateView, UserRestorePassView
from apps.users.views import MeView

urlpatterns = [
    path('/login', TokenObtainPairView.as_view(), name='auth_login'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path('/me', MeView.as_view(), name='auth_me'),
    path('/activate/<str:token>', UserActivateView.as_view(), name='auth_activate'),
    path('/reset/<str:token>', UserRestorePassView.as_view(), name='auth_reset'),
    path('/forget_pass', ForgetPassView.as_view(), name='auth_forget_pass'),
]
