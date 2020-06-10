from django.shortcuts import render
from django.http import HttpResponse
from .models import Video

def hello(request):
    return HttpResponse("<h1>Hello</h1>")

def world(request):
    response = {"name":"Yura","z":1}
    response["content"] = Video.objects.all()
    return render(request, "index.html", response)
# Create your views here.
