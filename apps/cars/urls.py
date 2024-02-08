from django.urls import path

from .views import CarAddPhotoView, CarsListCreateView, CarsRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarsListCreateView.as_view(), name='cars_list_create'),
    path('/<int:pk>', CarsRetrieveUpdateDestroyView.as_view(), name='cars_retrieve_update_destroy'),
    path('/<int:pk>/car_photo', CarAddPhotoView.as_view(), name='cars_add_photo'),
]
