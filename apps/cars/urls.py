from django.urls import path

from .views import CarsListCreateView, CarsRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarsListCreateView.as_view(), name='cars_list_create'),
    path('/<int:pk>', CarsRetrieveUpdateDestroyView.as_view(), name='cars_retrieve_update_destroy')
]
