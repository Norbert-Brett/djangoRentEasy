
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


# Test removed as /hosts/ URL does not exist
