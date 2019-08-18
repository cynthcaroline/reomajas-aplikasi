from django.urls import path

from . import views

urlpatterns = [
    path('', views.makanan, name='index'),
        #yang ditambahi
    path('report/', views.report, name='report'),
]
