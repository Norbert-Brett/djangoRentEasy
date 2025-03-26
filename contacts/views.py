# Import necessary modules from Django
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import render_to_string

# Import the Contact model from the current directory
from .models import Contact


# Function to send an email notification
def send_notification(mail_subject, mail_template, context):
    # Get the default from email from settings
    from_email = settings.DEFAULT_FROM_EMAIL
    # Render the email message using the provided template and context
    message = render_to_string(mail_template, context)
    # If the to_email in the context is a string, convert it to a list
    if isinstance(context['to_email'], str):
        to_email = [context['to_email']]
    else:
        to_email = context['to_email']
    # Create an EmailMessage object and send it
    mail = EmailMessage(mail_subject, message, from_email, to=to_email)
    mail.content_subtype = "html"
    mail.send()


# View function for the contact form
def contact(request):
    # If the request method is POST
    if request.method == 'POST':
        # Get the form data from the request and store it in a context dictionary
        context = {
            'listing_id': request.POST['listing_id'],
            'listing': request.POST['listing'],
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'message': request.POST['message'],
            'user_id': request.POST['user_id'],
            'host_email': request.POST['host_email'],
            'to_email': [request.POST['host_email']],  # assuming the host_email is the recipient
        }

        # If the user is authenticated
        if request.user.is_authenticated:
            # Check if the user has already made an inquiry for this listing
            has_contacted = Contact.objects.all().filter(listing_id=context['listing_id'], user_id=context['user_id'])
            if has_contacted:
                # If the user has already made an inquiry, show an error message and redirect
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/' + context['listing_id'])

        # Create a new Contact object with the form data and save it to the database
        contact = Contact(listing=context['listing'], listing_id=context['listing_id'], name=context['name'],
                          email=context['email'], phone=context['phone'], message=context['message'],
                          user_id=context['user_id'])

        contact.save()

        # Send an email notification
        send_notification(
            'Property Listing Inquiry',
            'contact/email_template.html',
            context
        )

        # Show a success message and redirect
        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/' + context['listing_id'])
