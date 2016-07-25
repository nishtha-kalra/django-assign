from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    return HttpResponse("Hi!!")

def register(request):
    template = loader.get_template('register/register.html')
    return HttpResponse(template.render(request))
