from django.urls import path
from .views import calculate_sum

urlpatterns = [
    path("sum/", calculate_sum, name="calculate_sum"),
]
