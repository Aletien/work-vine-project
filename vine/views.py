from django.shortcuts import render
from .models import Team

def home(request):
    teams = Team.objects.all()
    data = {
        'teams' : teams,
    }
    return render(request, 'vine/home.html', data)



def about(request):
    teams = Team.objects.all()
    context = {
        'teams': teams,
    }
    return render(request, 'vine/about.html', context)


def services(request):

    return render(request, 'vine/services.html')



def contact(request):

    return render(request, 'vine/contact.html')


def store(request):
    return render(request, 'vine/store.html')
