from django.utils.decorators import method_decorator

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from .filters import CarFilter
from .models import CarModel
from .serializers import CarPhotoSerializer, CarSerializer


@method_decorator(name='get', decorator=swagger_auto_schema(security=[]))
@method_decorator(name='post', decorator=swagger_auto_schema(security=[], operation_id='jkhsdfhksf', operation_summary='create new car!!!'))
class CarsListCreateView(ListCreateAPIView):
    """
        get:
            List all cars
        post:
            Create a new car
    """
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilter
    permission_classes = (AllowAny,)
    pagination_class = None


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
