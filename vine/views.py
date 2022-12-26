from django.shortcuts import render

from store.models import Store
from .models import Team

def home(request):
    teams = Team.objects.all()
    featured = Store.objects.order_by('-created_date').filter(is_featured=True)
    all_stores = Store.objects.order_by('-created_date')
    data = {
        'teams' : teams,
        'featured' : featured,
        'all_stores' : all_stores,
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
