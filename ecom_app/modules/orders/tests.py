from base.test_global import TestGlobal
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from modules.orders.models import Order, OrderMvto


class OrderTestClass(TestCase):

    module_name = '/orders/'

    def test_api_list_order(self):

        user = TestGlobal.create_user_test()
        token = TestGlobal.get_token_test(user)
        orders = TestGlobal.create_order_test(user, 5)
        response = TestGlobal.api_list(self.module_name, token)
        response_data = response.json()

        self.assertIs(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_data.get('results', [])) > 0, True)
        self.assertContains(response, self.module_name)

    def test_api_create_order(self):

        user = TestGlobal.create_user_test()
        token = TestGlobal.get_token_test(user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=token)

        response = client.post(
            self.module_name,
            {'status': 'Nuevo', 'created_by': user.id}
        )

        self.assertIs(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.filter(
            id=response.json().get('id')).count() > 0, True)

    def test_api_create_order_mvto(self):

        user = TestGlobal.create_user_test()
        token = TestGlobal.get_token_test(user)
        order = TestGlobal.create_order_test(user, 1)
        product = TestGlobal.create_product_test(user, 1)

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=token)

        response = client.post(
            f"{self.module_name}{order.id}/create_order_mvto/",
            {'order': order.id, 'product': product.id,
                'cant': '5', 'created_by': user.id}
        )

        self.assertIs(response.status_code, status.HTTP_200_OK)
        self.assertEqual(OrderMvto.objects.filter(
            id=response.json().get('id')).count() > 0, True)

    def test_api_list_order_mvto(self):

        user = TestGlobal.create_user_test()
        token = TestGlobal.get_token_test(user)
        product = TestGlobal.create_product_test(user, 1)
        order = TestGlobal.create_order_test(user, 1, product, 2)

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=token)

        response = client.get(
            f"{self.module_name}{order.id}/list_order_mvto/"
        )

        self.assertIs(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json().get('results', [])) > 0, True)
