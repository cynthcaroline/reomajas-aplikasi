from django.urls import path

from . import views

urlpatterns = [
    path('', views.makanan, name='index'),
]