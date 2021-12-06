from base.test_global import TestGlobal
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from modules.shipments.models import Shipment, update_after, update_before
from django.utils import timezone


class ShipmentTestClass(TestCase):

    module_name = '/shipments/'

    def test_api_list_shipment(self):

        user = TestGlobal.create_user_test()
        token = TestGlobal.get_token_test(user)
        order = TestGlobal.create_order_test(user, 1)
        shipment = TestGlobal.create_shipment_test(user, 1, order)
        response = TestGlobal.api_list(self.module_name, token)
        response_data = response.json()
        
        self.assertIs(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_data.get('results', [])) > 0, True)

    def test_api_create_shipment(self):

        user = TestGlobal.create_user_test()
        token = TestGlobal.get_token_test(user)
        order = TestGlobal.create_order_test(user, 1)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=token)

        response = client.post(
            self.module_name,
            {'status': 'Nuevo', 'order': order.id, 'created_by': user.id}
        )

        self.assertIs(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Shipment.objects.filter(id=response.json().get('id')).count() > 0, True)

    def test_api_update_shipment(self):

        user = TestGlobal.create_user_test()
        token = TestGlobal.get_token_test(user)
        order = TestGlobal.create_order_test(user, 1)
        shipment = TestGlobal.create_shipment_test(user, 1, order)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=token)

        product = TestGlobal.create_product_test(user, 1)
        product_name = product.name

        response = client.put(
            f"{self.module_name}{shipment.id}/",
            {'status': 'Despachado', 'created_by': user.id}
        )
        
        self.assertIs(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('name') != product_name, True)