from django.shortcuts import render
from django.template import RequestContext
# Create your views here.
def landingPage(request):
    return render(request,'index.html',{'STATIC_URL':'../static/'})