from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate

# Create your views here.

def index(request):
    context = {'key':2};
    return render(request,'index.html', context);

def notFound(request):
    return HttpResponse("Sorry page not found. Currently only base url at / is defined");

def authentication(request):
    try:
        username = request.POST['username'];
        password = request.POST['password'];
        user = authenticate(username = username, password = password)
        if user is not None:
            return HttpResponse("Yes ! You are authenticated !!!");
        else:
            return HttpResponse("Invalid credentials given");
    except Exception as e:
        print(e);
        return HttpResponse("Invalid input given. Cannot authenticate user !!!");
