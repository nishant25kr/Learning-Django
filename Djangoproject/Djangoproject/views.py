from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello world,you are a good person")
    return render(request, 'website/one.html')

def about(request):
    return HttpResponse("Hello world,you are a good person,About page")

def contact(request):
    return HttpResponse("Hello world,you are a good person,Contact page")