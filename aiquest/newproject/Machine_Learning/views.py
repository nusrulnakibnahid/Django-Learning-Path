from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def machine_learning(request):
    return HttpResponse("<h1>This is machine learning</h1>")
