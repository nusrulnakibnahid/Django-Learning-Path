from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def deep_learning(request):
    # learning = {'dl': 'Deep Learning'} # this a single way to send data to template

    a = 10
    b = 5
    c = 'knowledge'
    d = 'deep learning'

    abc = {'a': a, 'b': b, 'c': c, 'dl': d}
    return render(request, 'deep_learning/deep_learning.html', context=abc)


