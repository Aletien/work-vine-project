from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from store.models import Store

def store(request):
    furnitures = Store.objects.order_by('-created_date')
    paginator = Paginator(furnitures, 6)
    page = request.GET.get('page')
    paged_furnitures = paginator.get_page(page)
    condition_search = Store.objects.values_list('condition', flat=True).distinct
    body_style_search = Store.objects.values_list('body_style', flat=True).distinct
    city_search = Store.objects.values_list('city', flat=True).distinct
    color_search = Store.objects.values_list('color', flat=True).distinct
    year_search = Store.objects.values_list('year', flat=True).distinct
    data = {
        'furnitures' : paged_furnitures,
        'condition_search': condition_search,
        'body_style_search' : body_style_search,
        'city_search' : city_search,
        'color_search' : color_search,
        'year_search': year_search,
    }
    return render(request, 'store/store.html', data)

def store_detail(request, id):
    single_furniture = get_object_or_404(Store, pk=id)
    data = {
        'single_furniture' : single_furniture,
    }
    return render(request, 'store/store_details.html', data)

def search(request):
    furnitures = Store.objects.order_by('-created_date')
    condition_search = Store.objects.values_list('condition', flat=True).distinct
    body_style_search = Store.objects.values_list('body_style', flat=True).distinct
    city_search = Store.objects.values_list('city', flat=True).distinct
    color_search = Store.objects.values_list('color', flat=True).distinct
    year_search = Store.objects.values_list('year', flat=True).distinct

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            furnitures = furnitures.filter(title__icontains=keyword)

    if 'condition' in request.GET:
        condition = request.GET['condition']
        if condition:
            furnitures = furnitures.filter(condition__iexact=condition)
    
    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            furnitures = furnitures.filter(body_style__iexact=body_style)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            furnitures = furnitures.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            furnitures = furnitures.filter(year__iexact=year)        

    if 'color' in request.GET:
        color = request.GET['color']
        if color:
            furnitures = furnitures.filter(color__iexact=color)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            furnitures = furnitures.filter(price__gte=min_price, price__lte=max_price)        
    data = {
        'furnitures' : furnitures,
        'condition_search': condition_search,
        'body_style_search' : body_style_search,
        'city_search' : city_search,
        'color_search' : color_search,
        'year_search': year_search,
    }
    return render(request, 'store/search.html', data)