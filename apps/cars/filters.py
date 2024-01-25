from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from .models import CarModel
from .serializers import CarSerializer


def cars_filter(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()
    for key, value in query.items():
        match key:
            case 'price_gt':
                qs = qs.filter(price__gt=value)
            case 'price_gte':
                qs = qs.filter(price__gte=value)
            case 'price_lt':
                qs = qs.filter(price__lt=value)
            case 'price_lte':
                qs = qs.filter(price__lte=value)

            case 'year_gt':
                qs = qs.filter(year__gt=value)
            case 'year_gte':
                qs = qs.filter(year__gte=value)
            case 'year_lt':
                qs = qs.filter(year__lt=value)
            case 'year_lte':
                qs = qs.filter(year__lte=value)

            case 'brand_start':
                qs = qs.filter(brand__istartswith=value)
            case 'brand_end':
                qs = qs.filter(brand__iendswith=value)
            case 'brand_contains':
                qs = qs.filter(brand__icontains=value)

            case 'order':
                fields = CarSerializer.Meta.fields
                fields = [*fields, *[f'-{field}' for field in fields]]

                if value not in fields:
                    raise ValidationError({'details': f'Please choice order from {", ".join(fields)}'})
                qs = qs.order_by(value)
            case _:
                raise ValidationError({'Details': f'{key} is not a allowed here'})
    return qs
