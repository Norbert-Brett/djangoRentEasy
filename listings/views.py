from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing


def index(request):
    listings = Listing.objects.order_by('-list_date')

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    try:
        paged_listings = paginator.get_page(page)
    except PageNotAnInteger:
        # Fallback to the first page
        paged_listings = paginator.get_page(1)
    except EmptyPage:
        # Fallback to the last page
        paged_listings = paginator.get_page(paginator.num_pages)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    listings = Listing.objects.order_by('-list_date')

    city_search = Listing.objects.values_list('city', flat=True).distinct()
    country_search = Listing.objects.values_list('country', flat=True).distinct()
    bedroom_search = Listing.objects.values_list('bedrooms', flat=True).distinct()
    price_search = Listing.objects.values_list('price', flat=True).distinct()
    bathroom_search = Listing.objects.values_list('bathrooms', flat=True).distinct()

    # City or Country
    if 'city' in request.GET:
        city = request.GET.get('city')
        if city:
            listings = listings.filter(city__iexact=city)

    # Country
    if 'country' in request.GET:
        country = request.GET.get('country')
        if country:
            listings = listings.filter(country__iexact=country)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            listings = listings.filter(bedrooms__iexact=bedrooms)

    # Bathrooms
    if 'bathrooms' in request.GET:
        bathrooms = request.GET['bathrooms']
        if bathrooms:
            listings = listings.filter(bathrooms__iexact=bathrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            listings = listings.filter(price__lte=price)

    paginator = Paginator(listings, 3)  # Show 6 listings per page
    page = request.GET.get('page')

    try:
        paged_listings = paginator.page(page)
    except PageNotAnInteger:
        paged_listings = paginator.page(1)
    except EmptyPage:
        paged_listings = paginator.page(paginator.num_pages)

    context = {
        'listings': paged_listings,  # Update context to use paged_listings
        'city_search': city_search,
        'country_search': country_search,
        'bedroom_search': bedroom_search,
        'bathroom_search': bathroom_search,
        'price_search': price_search,
    }

    return render(request, 'listings/search.html', context)
