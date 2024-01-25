from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from .filters import cars_filter
from .models import CarModel
from .serializers import CarSerializer


class CarsListCreateView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        return cars_filter(self.request.query_params)


class CarsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
