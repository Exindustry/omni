from rest_framework.test import APIClient


class TestGlobal:

    def get_token_test(user):

        from rest_framework.authtoken.models import Token

        token, token_create = Token.objects.get_or_create(user=user)
        return "Token " + token.key

    def create_user_test():

        from modules.users.models import User

        fields = {'username': 'demo', 'password': 'demo.1423',
                  'email': 'cardona.zero@gmail.com', 'name': 'demo', 'last_name': 'demo'}

        base_obj = User.objects.create_user(**fields)
        base_obj.save()
        return base_obj

    def create_payment_test(user, order):

        from modules.payments.models import Payment, PaymentMvto

        fields = {"name": "P2", "amount": 10000.0,"created_by": user,"orders": [{"order": order,"amount": 7000.0},{"order": order,"amount": 3000.0}]}
        fields_copy = fields.copy()
        del fields_copy['orders']

        base_obj = Payment.objects.create(**fields_copy)

        for row in fields.get('orders'):
            PaymentMvto.objects.create(**row, payment=base_obj)

        return base_obj

    def create_shipment_test(user, cant=1, order=None):

        from modules.shipments.models import Shipment

        fields = {'status': 'Nuevo', 'order': order, 'created_by': user}

        for row in range(cant):
            base_obj = Shipment.objects.create(**fields)
            base_obj.save()

        return base_obj

    def create_product_test(user, cant=1):

        from modules.products.models import Product

        fields = {'name': 'Rust', 'price': float(
            10000), 'category': 'Video Juego', 'description': 'Rust', 'created_by': user}

        for row in range(cant):
            base_obj = Product.objects.create(**fields)
            base_obj.save()

        return base_obj

    def create_order_test(user, cant=1, product=None, mvto=0):

        from modules.orders.models import Order, OrderMvto

        fields = {'status': 'Nuevo', 'created_by': user}

        for row in range(cant):
            base_obj = Order.objects.create(**fields)
            base_obj.save()

            if product:
                mvto_fields = {'order': base_obj, 'product': product,
                            'cant': '2', 'created_by': user}

                for mv in range(mvto):
                    mvto_base_obj = OrderMvto.objects.create(**mvto_fields)

        return base_obj

    def api_list(module, token):
        token = token
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=token)
        response = client.get(module, {}, format='json')

        return response
