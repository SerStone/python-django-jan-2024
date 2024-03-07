from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from apps.auto_parks.models import AutoParkModel
from apps.auto_parks.serializers import AutoParkWithOutCarsSerializer
from apps.cars.serializers import CarSerializer


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkWithOutCarsSerializer
    permission_classes = (AllowAny,)


class AutoParkAddCarView(GenericAPIView):
    queryset = AutoParkModel.objects.all()

    def post(self, request, *args, **kwargs):
        auto_park = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        ap_serializer = AutoParkWithOutCarsSerializer(auto_park)
        return Response(ap_serializer.data, status=status.HTTP_201_CREATED)


class AutoParkRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkWithOutCarsSerializer


