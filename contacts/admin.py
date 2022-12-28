from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'item_title', 'town', 'city', 'user_id', 'created_date')
    list_display_links = ('id', 'first_name', 'last_name', 'email')
    list_filter = ('first_name', 'last_name', 'email', 'item_title', 'town', 'city', 'created_date')
    search_fields = ('first_name', 'last_name', 'email', 'item_title', 'town', 'city')
    list_per_page = 6


admin.site.register(Contact, ContactAdmin)
