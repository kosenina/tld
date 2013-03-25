# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request, 'main/login.html')

def home(request):
    return HttpResponse("You're at the home page.")

def profile(request):
    return HttpResponse("You're at the profile page.")

def article(request):
    return HttpResponse("You're at the article page.")

