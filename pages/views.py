from django.shortcuts import render

from listings.models import Listing


def index(request):
    listings = Listing.objects.order_by('-list_date')[:3]

    context = {
        'listings': listings,
    }

    return render(request, 'pages/index.html', context)


def about(request):

    return render(request, 'pages/about.html')
