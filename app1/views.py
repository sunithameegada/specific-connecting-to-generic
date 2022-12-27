from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def loki(request):
    return HttpResponse('<h1><marquee>loki is my best frnd</marquee></h1>')
