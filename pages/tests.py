
# pages/tests.py
from django.test import TestCase
from .models import Page


class PageModelTest(TestCase):
    def test_page_creation(self):
        page = Page.objects.create(
            title='Test Page',
            content='Test content'
        )
        self.assertEqual(Page.objects.count(), 1)
        self.assertEqual(page.title, 'Test Page')
        self.assertEqual(page.content, 'Test content')

    def test_page_str_representation(self):
        page = Page.objects.create(
            title='Test Page',
            content='Test content'
        )
        self.assertEqual(str(page), 'Test Page')


class PageViewTest(TestCase):
    def test_page_view(self):
        # Create a page
        page = Page.objects.create(
            title='Test Page',
            content='Test content'
        )

        # Test the view
        response = self.client.get('/pages/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Page')
        self.assertContains(response, 'Test content')
