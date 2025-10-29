from django.urls import path
from . import views

urlPatterns = [
    path('function', views.hello_world),
    path('class', views.HelloCanada.as_view())
]