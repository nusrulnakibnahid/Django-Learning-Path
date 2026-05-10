from django.shortcuts import render
from django.http import HttpResponse
from About_Us.models import Teachers

# Create your views here.
def about_us(request):

    abt = 'about us'
    dtl = 'details'
    update = {'a':abt, 'd':dtl}
    return render(request, 'about/about.html',context=update)



def teachers_info(request):
    teach = Teachers.objects.all()
    return render (request, 'about/t.html', {'thr': teach})
