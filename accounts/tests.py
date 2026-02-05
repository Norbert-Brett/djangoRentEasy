from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.dashboard_url = reverse('dashboard')

        self.user = User.objects.create_user('testuser1', password='12345')

    def test_register_GET(self):
        response = self.client.get(self.register_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_register_POST(self):
        response = self.client.post(self.register_url, {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser2',
            'email': 'testuser2@example.com',
            'password': '12345',
            'password2': '12345'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.last().username, 'testuser2')

    def test_login_GET(self):
        response = self.client.get(self.login_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_login_POST(self):
        self.client.login(username='testuser1', password='12345')

        response = self.client.post(self.login_url, {
            'username': 'testuser1',
            'password': '12345'
        })

        self.assertEqual(response.status_code, 302)

    def test_logout_POST(self):
        self.client.login(username='testuser1', password='12345')

        response = self.client.post(self.logout_url)

        self.assertEqual(response.status_code, 302)

    def test_dashboard_GET(self):
        self.client.login(username='testuser1', password='12345')

        response = self.client.get(self.dashboard_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/dashboard.html')