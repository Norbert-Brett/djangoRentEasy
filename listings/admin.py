from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'host')
    list_display_links = ('id', 'title')
    list_filter = ('host',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'city', 'country', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
