from base.test_global import TestGlobal
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from modules.products.models import Product


class ProductTestClass(TestCase):

    module_name = '/products/'

    def test_api_list_product(self):

        user = TestGlobal.create_user_test()
        token = TestGlobal.get_token_test(user)
        product = TestGlobal.create_product_test(user, 5)
        response = TestGlobal.api_list(self.module_name, token)
        response_data = response.json()

        self.assertIs(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_data.get('results', [])) > 0, True)
        self.assertContains(response, self.module_name)

    def test_api_create_product(self):

        user = TestGlobal.create_user_test()
        token = TestGlobal.get_token_test(user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=token)

        response = client.post(
            self.module_name,
            {'name': 'Rust', 'price': float(
                10000), 'category': 'Video Juego', 'description': 'Rust', 'created_by': user.id}
        )

        self.assertIs(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.filter(id=response.json().get('id')).count() > 0, True)

    def test_api_update_product(self):

        user = TestGlobal.create_user_test()
        token = TestGlobal.get_token_test(user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=token)

        product = TestGlobal.create_product_test(user, 1)
        product_name = product.name

        response = client.put(
            f"{self.module_name}{product.id}/",
            {'name': 'FF14', 'created_by': user.id, 'price': float(10), 'category': 'Video Juego'}
        )
        
        self.assertIs(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('name') != product_name, True)

    def test_api_delete_product(self):

        user = TestGlobal.create_user_test()
        token = TestGlobal.get_token_test(user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=token)

        product = TestGlobal.create_product_test(user, 1)

        response = client.delete(
            self.module_name  + str(product.id) + '/'
        )
        
        self.assertIs(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.all().count() == 0, True)
    