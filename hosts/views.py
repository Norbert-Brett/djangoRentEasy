from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from listings.models import Listing
from contacts.models import Contact
from hosts.models import Host


@login_required
def host_dashboard(request):
    """Host dashboard showing their listings and messages"""
    try:
        # Get or create host profile for the user
        host = Host.objects.get(user=request.user)
    except Host.DoesNotExist:
        # User is not a host
        messages.error(request, 'You need to be registered as a host to access this page.')
        return redirect('dashboard')
    
    # Get all listings for this host
    host_listings = Listing.objects.filter(host=host).order_by('-list_date')
    
    # Get all messages for this host's listings
    listing_ids = host_listings.values_list('id', flat=True)
    host_messages = Contact.objects.filter(listing_id__in=listing_ids).order_by('-contact_date')
    
    # Calculate stats
    total_listings = host_listings.count()
    published_listings = host_listings.filter(is_published=True).count()
    total_messages = host_messages.count()
    unread_messages = host_messages.filter(user_id=request.user.id).count()  # Simplified unread logic
    
    context = {
        'host': host,
        'listings': host_listings,
        'messages': host_messages,
        'total_listings': total_listings,
        'published_listings': published_listings,
        'total_messages': total_messages,
        'unread_messages': unread_messages,
    }
    
    return render(request, 'hosts/dashboard.html', context)
