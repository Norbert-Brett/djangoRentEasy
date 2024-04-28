from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing


# Function to display the listings page
def index(request):
    # Get all listings ordered by list date
    listings = Listing.objects.order_by('-list_date')

    # Create a paginator object with 6 listings per page
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    try:
        # Try to get the requested page
        paged_listings = paginator.get_page(page)
    except PageNotAnInteger:
        # If the page is not an integer, show the first page
        paged_listings = paginator.get_page(1)
    except EmptyPage:
        # If the page is out of range, show the last page
        paged_listings = paginator.get_page(paginator.num_pages)

    context = {
        'listings': paged_listings
    }

    # Render the listings page with the context
    return render(request, 'listings/listings.html', context)


# Function to display a single listing
def listing(request, listing_id):
    # Get the listing or return a 404 error if not found
    listing = get_object_or_404(Listing, pk=listing_id)
    if request.method == 'POST':
        if 'listing_id' in request.POST:
            # Handle the 'listing_id' here
            pass
        else:
            # Return a 400 error if 'listing_id' is not in POST data
            return HttpResponseBadRequest("Bad Request: No listing_id field in POST data")
    context = {
        'listing': listing,
        'listing_id': listing_id,
        'listing_title': listing.title
    }

    # Render the listing page with the context
    return render(request, 'listings/listing.html', context)


# Function to handle search
def search(request):
    # Get all listings ordered by list date
    listings = Listing.objects.order_by('-list_date')

    # Get distinct values for city, country, bedrooms, price, and bathrooms
    city_search = Listing.objects.values_list('city', flat=True).distinct()
    country_search = Listing.objects.values_list('country', flat=True).distinct()
    bedroom_search = Listing.objects.values_list('bedrooms', flat=True).distinct()
    price_search = Listing.objects.values_list('price', flat=True).distinct()
    bathroom_search = Listing.objects.values_list('bathrooms', flat=True).distinct()

    # Filter listings based on search criteria
    if 'city' in request.GET:
        city = request.GET.get('city')
        if city:
            listings = listings.filter(city__iexact=city)

    if 'country' in request.GET:
        country = request.GET.get('country')
        if country:
            listings = listings.filter(country__iexact=country)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            listings = listings.filter(bedrooms__iexact=bedrooms)

    if 'bathrooms' in request.GET:
        bathrooms = request.GET['bathrooms']
        if bathrooms:
            listings = listings.filter(bathrooms__iexact=bathrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            listings = listings.filter(price__lte=price)

    # Create a paginator object with 3 listings per page
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')

    try:
        # Try to get the requested page
        paged_listings = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer, show the first page
        paged_listings = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, show the last page
        paged_listings = paginator.page(paginator.num_pages)

    context = {
        'listings': paged_listings,
        'city_search': city_search,
        'country_search': country_search,
        'bedroom_search': bedroom_search,
        'bathroom_search': bathroom_search,
        'price_search': price_search,
    }

    # Render the search page with the context
    return render(request, 'listings/search.html', context)
