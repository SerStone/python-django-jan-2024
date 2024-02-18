from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from core.models import BaseModel
from core.services.upload_avatar import upload_avatar

from apps.users.managers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):

    class Meta:
        db_table = 'auth_user'
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=(('M', 'Male'), ('F', 'Female'), ('U', 'Unknown')))
    phone_number = models.CharField(max_length=10)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(blank=True, upload_to=upload_avatar)
