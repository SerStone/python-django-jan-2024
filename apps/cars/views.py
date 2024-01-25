
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import CarModel
from .serializers import CarSerializer
from .filters import cars_filter


class CarsListCreateView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        return cars_filter(self.request.query_params)


class CarsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
