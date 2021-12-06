from base.test_global import TestGlobal
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from modules.payments.models import Payment, PaymentMvto
import json


class PaymentTestClass(TestCase):

    module_name = '/payments/'

    def test_api_create_payment(self):

        user = TestGlobal.create_user_test()
        token = TestGlobal.get_token_test(user)
        order = TestGlobal.create_order_test(user, 1)

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=token)

        response = client.post(
            self.module_name,
            json.dumps({"name": "P3", "amount": 10000, "created_by": user.id, "orders": [
                       {"order": order.id, "amount": 7000}, {"order": order.id, "amount": 3000}]}),
            content_type='application/json'
        )

        self.assertIs(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Payment.objects.filter(
            id=response.json().get('id')).count() > 0, True)

        for row in response.json().get('orders'):
            order_id = row[-1:]
            self.assertEqual(PaymentMvto.objects.filter(
                order_id=order_id, payment_id=response.json().get('id')).count() > 0, True)


    def test_api_get_payment(self):

        user = TestGlobal.create_user_test()
        token = TestGlobal.get_token_test(user)
        order = TestGlobal.create_order_test(user, 1)
        payment = TestGlobal.create_payment_test(user, order)

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=token)

        response = client.post(
            f"{self.module_name}{payment.id}/list_payment_mvto/"
        )

        self.assertIs(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json().get('results', [])) > 0, True)