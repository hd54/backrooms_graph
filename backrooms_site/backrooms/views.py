from django.shortcuts import render
from django.http import HttpResponse
from .models import Level


# Create your views here.

# basic template
def index(request):
    return HttpResponse('')


# TODO: front-end work needed for template.html
def view(request):
    data = Level.objects.all()
    return render(request, 'your_template.html', {'data': data})
