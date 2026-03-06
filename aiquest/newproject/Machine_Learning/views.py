from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def machine_learning(request):
    course = 'machine learning'
    Tclass = 21
    seat = 20
    cduaration = '2.5 months'
    offering = {'c':course, 'tl':Tclass, 'st':seat, 'cd':cduaration}
    return render(request, 'machine_learning/machine_learning.html',context=offering)



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
    
