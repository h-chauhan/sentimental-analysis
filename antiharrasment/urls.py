from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'is_harrassing/$', get_is_harrassing),
    url(r'add_query/$', add_query)
]