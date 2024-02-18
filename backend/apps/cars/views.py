from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from .filters import CarFilter
from .models import CarModel
from .serializers import CarPhotoSerializer, CarSerializer


class CarsListCreateView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilter
    permission_classes = (AllowAny,)


class CarsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class CarAddPhotoView(UpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CarPhotoSerializer
    http_method_names = ('put',)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return CarModel.objects.get(pk=pk)

    def perform_update(self, serializer):
        car_instance = self.get_object()
        car_instance.car_photo.delete()
        super().perform_update(serializer)
