from django.shortcuts import render

from store.models import Store
from .models import Team

def home(request):
    teams = Team.objects.all()
    featured = Store.objects.order_by('-created_date').filter(is_featured=True)
    all_stores = Store.objects.order_by('-created_date')
    #search_fields = Store.objects.values('condition', 'body_style', 'city', 'color', 'year', 'price')
    condition_search = Store.objects.values_list('condition', flat=True).distinct
    body_style_search = Store.objects.values_list('body_style', flat=True).distinct
    city_search = Store.objects.values_list('city', flat=True).distinct
    color_search = Store.objects.values_list('color', flat=True).distinct
    year_search = Store.objects.values_list('year', flat=True).distinct
    data = {
        'teams' : teams,
        'featured' : featured,
        'all_stores' : all_stores,
       # 'search_fields' : search_fields,
        'condition_search': condition_search,
        'body_style_search' : body_style_search,
        'city_search' : city_search,
        'color_search' : color_search,
        'year_search': year_search,

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
