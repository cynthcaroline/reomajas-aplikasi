from django.urls import path

from . import views

urlpatterns = [
    path('', views.makanan, name='index'),
        #yang ditambahi
    path('hasil_json/', views.hasil_json, name='hasil_json'),
]
