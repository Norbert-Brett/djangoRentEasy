from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import Listing
from hosts.models import Host


def index(request):
    listings = Listing.objects.order_by('-list_date')[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all hosts
    hosts = Host.objects.order_by('-host_since')

    context = {
        'hosts': hosts,
    }

    return render(request, 'pages/about.html', context)
