from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def machine_learning(request):
    return render(request, 'machine_learning.html')


# def deep_learning(request):
    # return HttpResponse("<h1>This is deep learning </h1>")


# def about_us(request):
   # return HttpResponse("<h1>Thank you, This is about page</h1>")





def random(request):
    return render(request, 'machine_learning/random_forest.html')


def K_nearest(request):
    return render(request, 'machine_learning/knn.html')


def dtree(request):
    return render(request, 'machine_learning/dt.html')
    
