from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('<int:id>', views.car_detail, name='car_detail'),
]