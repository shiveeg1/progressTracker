from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.landingPage, name='landingPage'),
    url(r'^$',views.index, name='indexRoute'),
    url(r'^authenticate',views.authentication, name='authentication'),
    url(r'.*',views.notFound,name='No Match'),
]
