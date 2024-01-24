from django.db import models


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20)
    cabin_type = models.CharField(max_length=20)
    year = models.IntegerField()
    count_of_saddles = models.IntegerField()
    engine_type = models.FloatField()
    price = models.IntegerField()


#- марка машини
# - рік випуску
# - кількість місць
# - тип кузову
# - об'єм двигуна (float)
