from django.shortcuts import render
from .models import Link


def home(request):
    context = {
        'links': Link.objects.all()
    }
    return render(request, 'shortner/home.html', context)

def about(request):
    return render(request, 'shortner/about.html', {'title':'About'})