from django.test import TestCase, Client
from django.urls import reverse
from listings.models import Listing


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        from hosts.models import Host
        self.host = Host.objects.create(
            name='Test Host',
            phone='123456',
            email='test@test.com',
            photo='host.jpg'
        )
        self.listing1 = Listing.objects.create(
            host=self.host,
            title='Test Listing 1',
            city='Test City',
            country='Test Country',
            bedrooms=3,
            bathrooms=2,
            price=100000,
            photo_main='test.jpg'
        )

    def test_index_GET(self):
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listings/listings.html')
        self.assertTrue('listings' in response.context)

    def test_listing_GET(self):
        response = self.client.get(reverse('listing', args=[self.listing1.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listings/listing.html')
        self.assertTrue('listing' in response.context)

    def test_listing_GET_no_listing(self):
        response = self.client.get(reverse('listing', args=[100]))

        self.assertEqual(response.status_code, 404)

    def test_search_GET(self):
        response = self.client.get(reverse('search') + '?city=Test+City')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listings/search.html')
        self.assertTrue('listings' in response.context)
        self.assertEqual(len(response.context['listings']), 1)
