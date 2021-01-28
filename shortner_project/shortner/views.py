from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<a href="https://google.com">Go to google</a>')

def about(request):
    return HttpResponse('<h1>About Page</h1>')