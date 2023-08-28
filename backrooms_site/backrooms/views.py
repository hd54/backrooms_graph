from django.http import HttpResponse
from rest_framework import generics
from .models import Level
from .serializers import LevelSerializer


# Create your views here.
# basic template
def index(request):
    return HttpResponse('')


class LevelView(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
