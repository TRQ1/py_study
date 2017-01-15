import datetime


from django.http import HttpResponse
from django.views.generic.base import View

class HelloWorld_View:
    def hello(request):
        return HttpResponse('Hello, World!')
    def index(request):
        return HttpResponse('Home page')
    def currenttime(request):
        d = datetime.datetime.now()
        return HttpResponse("Current Time : {0}".format(d))
