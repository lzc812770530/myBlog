from django.conf.urls import url
from django.urls import path
from rest_framework.generics import GenericAPIView
from .views import *


urlpatterns = [
    url(r'[0-9]{4}',artical_views),
]







