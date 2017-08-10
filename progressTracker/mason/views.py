from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from models import *

from django.template import RequestContext


def landingPage(request):
    return render(request,'login.html',{'STATIC_URL':'../static/'})

def index(request):
    context = {'key':2};
    return render(request,'login.html', context);

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

<<<<<<< HEAD

def signupVerification(username, email):
    # if user already exits return 1
    user = User.objects.get(username=username, email=email)
    if User.objects.filter(username=username, email=email).exists():
        return 1
    # if username is taken return 2
    if User.objects.filter(username=username).exists():
        return 2


def signUp(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/homepage/')
    if request.method == "POST":
        username = request.get('username')
        email = request.get('email')
        if signupVerification(username,email) == 1:
           return HttpResponse(request,'signUp.html',{'verificationMsg' :'The user already exists. Please login.' })
        elif signupVerification(username,email) == 2:
            return HttpResponse(request,'signUp.html',{'verificationMsg' :'The username is unavailable. Please try another name.' })
        if request.method == "POST":
            username = request.get('username')
            password = request.get('password')
            firstName = request.get('firstName')
            lastName  = request.get('lastName')
            User.objects.create_user(username,email=email,password=password, first_name=firstName, last_name=lastName)
            return HttpResponse(0)
    return HttpResponse(1)
