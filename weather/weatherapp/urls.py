from django.urls import path
from weatherapp import views

urlpatterns = [
    path('', views.get_weather, name='get_weather'),
]
