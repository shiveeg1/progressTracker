from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'key':2};
    return render(request,'index.html', context);

def notFound(request):
    return HttpResponse("Sorry page not found. Currently only base url at / is defined");