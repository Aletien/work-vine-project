from django.contrib import admin
from .models import Store
from django.utils.html import format_html

class StoreAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.photo.url))
    thumbnail.short_description = 'Furniture image'
    list_display = ('id', 'thumbnail', 'title', 'village', 'city', 'color', 'condition', 'price', 'features', 'number_seats', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'title')
    search_fields = ('title', 'color', 'condition', 'number_seats')
    list_filter = ('title', 'city', 'color', 'condition', 'price', 'features', 'number_seats', 'created_date')
    list_editable = ('is_featured',)

admin.site.register(Store, StoreAdmin)
