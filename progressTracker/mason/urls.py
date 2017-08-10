from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.landingPage, name='landingPage'),
    url(r'^$',views.index, name='login'),
    url(r'^signup$', views.signUp, name='signUp'),
    url(r'^authenticate',views.authentication, name='authentication'),
    url(r'.*',views.notFound,name='No Match'),
]
