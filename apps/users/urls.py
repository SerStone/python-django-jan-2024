from django.urls import path

from .views import (
    AdminToUserView,
    UserAddAvatarView,
    UserBlockView,
    UserCreateApiView,
    UserToAdminView,
    UserUnblockView,
)

urlpatterns = [
    path('', UserCreateApiView.as_view(), name='user_create'),
    path('/avatar', UserAddAvatarView.as_view(), name='user_avatar'),
    path('/<int:pk>/to_admin', UserToAdminView.as_view(), name='user_to_admin'),
    path('/<int:pk>/to_user', AdminToUserView.as_view(), name='admin_to_user'),
    path('/<int:pk>/block', UserBlockView.as_view(), name='user_block'),
    path('/<int:pk>/unblock', UserUnblockView.as_view(), name='user_unblock'),
]
