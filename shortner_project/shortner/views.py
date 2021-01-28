from django.shortcuts import render

links = [
    {
        'id': '1',
        'title': 'google class room',
        'long': 'https://www.google.com/google-classroom',
        'short': 'short.et/4J3',
        'created': 'June 23, 2020'
    },
    {
        'id': '2',
        'title': 'ebay watch',
        'long': 'https://www.ebay.com/b/Wristwatches/31387/bn_2408451',
        'short': 'short.et/4G6',
        'created': 'June 25, 2020'
    }
]

def home(request):
    context = {
        'links': links
    }
    return render(request, 'shortner/home.html', context)

def about(request):
    return render(request, 'shortner/about.html', {'title':'About'})