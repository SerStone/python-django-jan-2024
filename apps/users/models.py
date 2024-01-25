from django.db import models

from core.models import BaseModel


class UserModel(BaseModel):
    class Meta:
        db_table = 'users'

    username = models.CharField(max_length=20, unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=(('M', 'Male'), ('F', 'Female'), ('U', 'Unknown')))

