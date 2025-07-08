from django.http import HttpResponse

def Home(request):
    return HttpResponse("You are at chai aur code,Home page")

def About(request):
    return HttpResponse("You are at chai aur code,About page")

def Contact(request):
    return HttpResponse("You are at chai aur code,Contact page")

