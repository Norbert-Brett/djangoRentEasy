from django.test import TestCase, Client
from django.urls import reverse
from listings.models import Listing


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.listing1 = Listing.objects.create(
            title='Test Listing 1',
            city='Test City',
            country='Test Country',
            bedrooms=3,
            bathrooms=2,
            price=100000
        )

    def test_index_GET(self):
        response = self.client.get(reverse('index'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'listings/listings.html')
        self.assertTrue('listings' in response.context)

    def test_listing_GET(self):
        response = self.client.get(reverse('listing', args=[self.listing1.id]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'listings/listing.html')
        self.assertTrue('listing' in response.context)

    def test_listing_GET_no_listing(self):
        response = self.client.get(reverse('listing', args=[100]))

        self.assertEquals(response.status_code, 404)

    def test_search_GET(self):
        response = self.client.get(reverse('search') + '?city=Test+City')

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'listings/search.html')
        self.assertTrue('listings' in response.context)
        self.assertEquals(len(response.context['listings']), 1)
