from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def data_analysis(request):
    data = 'data analysis'
    le = 'learning'
    day = 30

    update = {'da': data, 'l': le, 'd': day}

    Teachers = {'names':['Shakib', 'Rabby', 'Nakib'] }
    # return render(request, 'data_analysis/data_analysis.html', context=update)

    return render(request, 'data_analysis/data_analysis.html', context=Teachers)


def analysis(request):
    return render(request, 'data_analysis/analysis.html')
