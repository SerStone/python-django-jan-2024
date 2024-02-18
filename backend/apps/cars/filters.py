from django_filters import rest_framework as filters

from apps.cars.models import CarModel


# CarModel.objects.filter(yea)
class CarFilter(filters.FilterSet):
    year_lt = filters.NumberFilter('year', lookup_expr='lt')
    year_gt = filters.NumberFilter('year', lookup_expr='gt')
    year_lte = filters.NumberFilter('year', lookup_expr='lte')
    year_gte = filters.NumberFilter('year', lookup_expr='gte')
    year_range = filters.NumberFilter('year', lookup_expr='range')

    brand = filters.CharFilter('brand',lookup_expr='icontains')

    price_lt = filters.NumberFilter('price', lookup_expr='lt')
    price_gt = filters.NumberFilter('price', lookup_expr='gt')
    price_lte = filters.NumberFilter('price', lookup_expr='lte')
    price_gte = filters.NumberFilter('price', lookup_expr='gte')
    price_range = filters.NumberFilter('price', lookup_expr='range')

    order = filters.OrderingFilter(
        fields=(
            'id',
            'brand',
            'year',
            'price',
        )
    )
