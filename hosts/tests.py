
# hosts/tests.py
from django.test import TestCase
from .models import Host


class HostModelTest(TestCase):
    def test_host_creation(self):
        host = Host.objects.create(
            name='Test Host',
            photo='test_photo.jpg',
            description='Test description',
            phone='1234567890',
            email='test@example.com'
        )
        self.assertEqual(Host.objects.count(), 1)
        self.assertEqual(host.name, 'Test Host')
        self.assertEqual(host.photo, 'test_photo.jpg')
        self.assertEqual(host.description, 'Test description')
        self.assertEqual(host.phone, '1234567890')
        self.assertEqual(host.email, 'test@example.com')

    def test_host_str_representation(self):
        host = Host.objects.create(
            name='Test Host',
            photo='test_photo.jpg',
            description='Test description',
            phone='1234567890',
            email='test@example.com'
        )
        self.assertEqual(str(host), 'Test Host')


class HostListViewTest(TestCase):
    def test_host_list_view(self):
        # Create some hosts
        Host.objects.create(
            name='Test Host 1',
            photo='test_photo1.jpg',
            description='Test description 1',
            phone='1234567890',
            email='test1@example.com'
        )
        Host.objects.create(
            name='Test Host 2',
            photo='test_photo2.jpg',
            description='Test description 2',
            phone='9876543210',
            email='test2@example.com'
        )

        # Test the view
        response = self.client.get('/hosts/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['hosts']), 2)
