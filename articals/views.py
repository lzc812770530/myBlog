from django.shortcuts import render

# Create your views here.


def artical_views(request):
    return render(request,'artical.html',locals())



