from django.urls import path
from . import views

urlpatterns = [
    path('backrooms', views.index, name='index'),
]