# Import necessary modules from Django
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact


# Function to handle user registration
def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check if username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                # Check if email already exists
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    # If everything is fine, create a new user
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


# Function to handle user login
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # If the user is authenticated, log them in and redirect to the dashboard
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


# Function to handle user logout
def logout(request):
    if request.method == 'POST':
        # Log out the user and redirect to the index page
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')


# Function to display the user dashboard
def dashboard(request):
    # Get all contacts for the current user, ordered by contact date
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    
    # Get saved listings with related listing data
    from listings.models import SavedListing
    saved_listings = SavedListing.objects.filter(user=request.user).select_related('listing').order_by('-created_at')
    saved_count = saved_listings.count()

    context = {
        'contacts': user_contacts,
        'saved_count': saved_count,
        'saved_listings': saved_listings,
    }
    return render(request, 'accounts/dashboard.html', context)
