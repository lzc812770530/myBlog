from django.urls import include
from django.urls import path
from rest_framework.generics import GenericAPIView
from .views import *

urlpatterns = [
    path('',index_views),
    path('page/1',index_views),
    path('page/2',page2_views),
    path('page/3',page3_views),
]



