from django.urls import path
from .views import calculate, latest_record

urlpatterns = [
    path("calculate/", calculate, name="calculate"),  
    path("latest/", latest_record, name="latest_record"),  # New endpoint
]
