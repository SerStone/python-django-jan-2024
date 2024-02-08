from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class IsSuperuser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff and request.user.is_superuser)
