from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def data_analysis(request):
    data = 'data analysis'
    le = 'learning'
    day = 30

    update = {'da': data, 'l': le, 'd': day}
    return render(request, 'data_analysis/data_analysis.html', context=update)
