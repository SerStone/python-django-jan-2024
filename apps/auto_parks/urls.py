from django.urls import path

from .views import AutoParkAddCarView, AutoParkListCreateView, AutoParkRetrieveUpdateDestroyView

urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='auto_park_list_create'),
    path('/<int:pk>/cars', AutoParkAddCarView.as_view(), name='auto_park_add_car'),
    path('/<int:pk>', AutoParkRetrieveUpdateDestroyView.as_view(), name='auto_park_retrieve_update_destroy')
]
