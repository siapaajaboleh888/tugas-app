from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())
    
def additional(request):
    template = loader.get_template('additional.html')
    return HttpResponse(template.render())
# Create your views here.