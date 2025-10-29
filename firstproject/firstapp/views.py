from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
# A function based view where each function are given paremeters, in the form of requests by the user
def hello_world(request):
    return HttpResponse("Hello World!")

class HelloCanada(View):
    def get(self, request):
        return HttpResponse("Hello Canada")