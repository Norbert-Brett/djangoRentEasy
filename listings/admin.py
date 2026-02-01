from django.contrib import admin

from .models import Listing, SavedListing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'host')
    list_display_links = ('id', 'title')
    list_filter = ('host',)
    list_editable = ('is_published',)
    search_fields = ('title', 'city', 'country', 'description')
    list_per_page = 25


class SavedListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'listing', 'created_at')
    list_display_links = ('id', 'user')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'listing__title')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
admin.site.register(SavedListing, SavedListingAdmin)
