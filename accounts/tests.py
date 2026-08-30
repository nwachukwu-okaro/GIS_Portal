from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse


class UserModelTests(TestCase):
    def test_user_uses_normalised_email_and_receives_profile(self):
        user = get_user_model().objects.create_user(
            email='Viewer@Example.COM',
            password='correct-horse-battery-staple',
        )
        self.assertEqual(user.email, 'viewer@example.com')
        self.assertIsNone(user.username)
        self.assertEqual(user.profile.user, user)

    def test_superuser_flags_are_enforced(self):
        user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='correct-horse-battery-staple',
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class AuthenticationFlowTests(TestCase):
    def setUp(self):
        self.password = 'correct-horse-battery-staple'
        self.user = get_user_model().objects.create_user(
            email='viewer@example.com',
            password=self.password,
        )

    def test_anonymous_catalogue_request_redirects_to_login(self):
        response = self.client.get(reverse('catalogue:search'))
        self.assertRedirects(
            response,
            f"{reverse('accounts:login')}?next={reverse('catalogue:search')}",
        )

    def test_user_can_sign_in_with_email(self):
        response = self.client.post(
            reverse('accounts:login'),
            {'username': self.user.email, 'password': self.password},
        )
        self.assertRedirects(response, reverse('catalogue:search'))

    def test_viewer_cannot_access_upload(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('catalogue:upload'))
        self.assertEqual(response.status_code, 403)

    def test_user_with_upload_permission_can_access_upload(self):
        permission = Permission.objects.get(
            content_type__app_label='accounts',
            codename='upload_data',
        )
        self.user.user_permissions.add(permission)
        self.client.force_login(self.user)
        response = self.client.get(reverse('catalogue:upload'))
        self.assertEqual(response.status_code, 200)

    def test_superuser_can_open_custom_user_admin(self):
        admin = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password=self.password,
        )
        self.client.force_login(admin)
        response = self.client.get(reverse('admin:accounts_user_add'))
        self.assertEqual(response.status_code, 200)
