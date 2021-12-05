from base.test_global import TestGlobal
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase


class UserTestClass(TestCase):

    def test_api_log_in(self):

        user = TestGlobal.create_user_test()
        client = APIClient()

        response = client.post(
            '/sign_in/', {'username': user.username, 'password': 'demo.1423'})
        response_data = response.json()
        self.assertIs(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response_data.get('authenticated', False))

        response = client.post(
            '/logout/', {'username': user.username, 'password': 'Errrr'})
        response_data = response.json()
        self.assertIs(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertFalse(response_data.get('autheanticated', None))

    def test_api_log_out(self):

        user = TestGlobal.create_user_test()
        token = TestGlobal.get_token_test(user)
        client = APIClient()

        response = client.post(
            '/logout/', {'username': user.username, 'password': 'demo.1423'})
        response_data = response.json()
        self.assertIs(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response_data.get('logout', None))
