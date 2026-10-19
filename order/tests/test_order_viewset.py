import json

from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token
from product.factories import CategoryFactory, ProductFactory
from order.factories import UserFactory, OrderFactory
from product.models import Product
from order.models import Order


class TestOrderViewSet(APITestCase):

    def setUp(self):
        # Roda antes de cada teste para popular o banco com dados de exemplo
        self.user = UserFactory()
        token = Token.objects.create(user=self.user)
        token.save()

        self.category = CategoryFactory(title="technology")
        self.product = ProductFactory(
            title="mouse", price=100, category=[self.category]
        )
        self.order = OrderFactory(product=[self.product])

    def test_order(self):
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        # Testa a requisição GET para listar os pedidos da API
        response = self.client.get(reverse("order-list", kwargs={"version": "v1"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Carrega o JSON retornado pela API
        order_data = json.loads(response.content)

        # Valida se os dados aninhados do produto e da categoria batem com o esperado
        self.assertEqual(
            order_data["results"][0]["product"][0]["title"], self.product.title
        )
        self.assertEqual(
            order_data["results"][0]["product"][0]["price"], self.product.price
        )
        self.assertEqual(
            order_data["results"][0]["product"][0]["active"], self.product.active
        )
        self.assertEqual(
            order_data["results"][0]["product"][0]["category"][0]["title"],
            self.category.title,
        )

    def test_create_order(self):
        user = UserFactory()
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        product = ProductFactory()

        # Monta o payload JSON enviando os IDs exigidos pela escrita (products_id e user)
        data = json.dumps({"products_id": [product.id], "user": user.id})

        # Executa uma requisição POST para criar um novo pedido
        response = self.client.post(
            reverse("order-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Verifica no banco de dados se o pedido foi salvo corretamente para o usuário
        created_order = Order.objects.get(user=user)
        self.assertEqual(created_order.user, user)
