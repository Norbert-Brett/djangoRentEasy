from django.test import TestCase, Client
from django.urls import reverse
from contacts.models import Contact
from django.contrib.auth.models import User


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='testuser1', password='12345')
        self.contact_url = reverse('contact')

    def test_contact_GET(self):
        response = self.client.get(self.contact_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/contact.html')

    def test_contact_POST(self):
        self.client.login(username='testuser1', password='12345')

        response = self.client.post(self.contact_url, {
            'listing_id': '1',
            'listing': 'Test Listing',
            'name': 'Test User',
            'email': 'testuser@example.com',
            'phone': '1234567890',
            'message': 'This is a test message',
            'user_id': self.user1.id,
            'host_email': 'host@example.com'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Contact.objects.first().name, 'Test User')
