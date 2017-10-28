from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'is_harassing/$', get_is_harassing),
    url(r'add_query/$', add_query)
]