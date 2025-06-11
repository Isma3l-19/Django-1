from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# a geeks function that returns a simple HttpResponse
def geeks_view(request):
    return HttpResponse("<h1>Welcome to Geeks for Geeks</h1>")

# an example
def example_view(request):
    return HttpResponse("<h1>This is an example view</h1>")