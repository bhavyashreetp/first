from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def srujana(request):
    return HttpResponse('<marquee><h1>hai good morning</h1></marquee>')


def revi(request):
    return HttpResponse('<marquee><b><h2>how are you </h1></b></marquee>')