from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about_us(request):

    abt = 'about us'
    dtl = 'details'

    update = {'a':abt, 'd':dtl}

    return render(request, 'about/about.html',context=update)
