from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<int:id>', views.store_detail, name='store_detail'),
    path('search', views.search, name='search'),
]
