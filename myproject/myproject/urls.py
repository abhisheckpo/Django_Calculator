from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my API!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('calculator1.urls')), 
    path('', home),  
]
