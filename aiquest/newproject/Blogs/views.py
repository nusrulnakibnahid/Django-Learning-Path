from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog1(request):
    b = {'b' : 'Blogs'}
    return render(request, 'blogs/blogs.html', context=b)
