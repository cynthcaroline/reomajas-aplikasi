from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_check, name='api_check'),
    path('recognize-food', views.recognize_food, name='recognize_food'),
    path('get-berat', views.get_berat, name='get_berat'),
]