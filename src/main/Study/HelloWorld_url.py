from django.conf.urls import url, include
from .HelloWorld_Django import HelloWorld_View

urlpatterns = url(r'^hello/$', HelloWorld_View)
