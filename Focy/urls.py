from django.urls import path
from . import views
from django.contrib.auth import views as auth
from django.contrib import admin
from django.conf.urls import url

app_name = "Focy"
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('project/', views.project, name='project'),
    path('service/', views.service, name='service'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('pay/', views.pay, name='pay'),
    path('token/', views.token, name='token'),
    path('stk/', views.stk, name='stk'),
]