from django.shortcuts import render

# Create your views here.


def index_views(request):
    return render(request,'index.html',locals())


def page2_views(request):
    return render(request, 'page2.html', locals())



def page3_views(request):
    return render(request, 'page3.html', locals())



