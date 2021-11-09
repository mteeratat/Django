from django import template
from django.http.response import HttpResponseGone
from django.shortcuts import render
from django.http import HttpResponse
from django.template import context, loader

# Create your views here.

# def index(request):
#     return HttpResponse("<h1>Hello, world</h1><b>Welcome to My Library</b>")

# def index(request):
#     header_str = 'Hello, Python variable'
#     template = loader.get_template('index.html')
#     context = {
#         'var1': header_str
#     }
#     return HttpResponse(template.render(context, request))

def index(request):
    header_str = 'Hello, Python variable'
    context = {
        'var1': header_str
    }
    return render(request, 'index.html', context)