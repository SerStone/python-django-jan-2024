from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from .filters import CarFilter
from .models import CarModel
from .serializers import CarSerializer


class CarsListCreateView(ListAPIView):
    queryset = CarModel.objects.get_only_tesla()
    serializer_class = CarSerializer
    filterset_class = CarFilter


class CarsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
