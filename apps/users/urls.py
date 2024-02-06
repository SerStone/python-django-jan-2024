from django.urls import path

from .views import UserCreateApiView

urlpatterns = [
    path('', UserCreateApiView.as_view(), name='user_create')
]
