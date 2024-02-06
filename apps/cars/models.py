from django.core import validators as V
from django.db import models

from core.enums.regex_enum import Regex
from core.models import BaseModel

from apps.auto_parks.models import AutoParkModel
from apps.cars.managers import CarManager


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('-id',)

    brand = models.CharField(max_length=20, validators=[V.RegexValidator(Regex.BRAND.pattern, Regex.BRAND.msg)])
    price = models.IntegerField(validators=[V.MinValueValidator(0), V.MaxValueValidator(1_000_000)])
    year = models.IntegerField(validators=[V.MinValueValidator(1900), V.MaxValueValidator(2024)])
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')

    objects = CarManager()
