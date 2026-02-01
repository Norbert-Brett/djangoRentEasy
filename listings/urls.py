from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>/', views.listing, name='listing'),
    path('search/', views.search, name='search'),
    path('save/<int:listing_id>/', views.save_listing, name='save_listing'),
    path('saved-status/<int:listing_id>/', views.get_saved_status, name='get_saved_status'),
]
