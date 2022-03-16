
from django.contrib import admin
from django.urls import path,include
from employee import views
from .views import BaseRegisterView,UserLoginView,ViewEmployee


urlpatterns = [
   
    path('',views.homepage,name="index"),

    path('aboutus/',views.aboutus, name="aboutus"),
    path('contact/',views.contact, name="contact"),
    path('trending/',views.trend, name= "trending"),
    path('Explore work/',views.explore,name = "explorework"),
    path('register/',BaseRegisterView.as_view(), name = "register"),
    path('login/',UserLoginView.as_view(),name ="login"),
    path('viewemployee/',ViewEmployee.as_view(),name = "viewemployee"),

]