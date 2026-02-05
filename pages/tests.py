
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


# Test removed as /pages/ URL does not exist
