from django.urls import path
from . import views
from .views import LevelView

urlpatterns = [
    path('', views.index, name='index'),
    path('api', LevelView.as_view(), name='api'),
]
