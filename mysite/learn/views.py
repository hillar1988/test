from django.shortcuts import render

# Create your views here.
# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse(u"<h1>PRC</h1><p>The People's Republic of China was born in 1949...</p>")

def index(request):
    return render(request, "index.html")

def home(request):
    list = ["html", "css", "botstrap", "python"]
    return render(request, 'home.html', {'list': list})

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))
