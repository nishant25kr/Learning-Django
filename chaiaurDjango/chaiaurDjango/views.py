from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    # return HttpResponse("You are at chai aur code,Home page")
    return render(request, 'index.html')


def About(request):
    return render(request, 'about.html')

def Contact(request):
    return HttpResponse("You are at chai aur code,Contact page")

