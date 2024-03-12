from django.urls import path

from .views import * 

urlpatterns = [
    path('', home, name="home"),
    path('uslugi/', uslugi, name="uslugi"),
    path('map/', map, name="map")
]
