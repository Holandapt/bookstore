from rest_framework import serializers

from order.models import Order
from product.models.product import Product
from product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    # Retorna os produtos detalhados usando o ProductSerializer;
    product = ProductSerializer(many=True, read_only=True)

    # Recebe uma lista de IDs de produtos para vincular ao pedido;
    products_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True, many=True
    )

    # Campo personalizado que calcula dinamicamente o valor total do pedido
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        # Soma o preço de todos os produtos associados a esta instância de pedido
        return sum([product.price for product in instance.product.all()])

    class Meta:
        model = Order
        fields = ["id", "user", "product", "total", "products_id"]

    def create(self, validated_data):
        # Extrai os IDs dos produtos e o usuário do payload validado
        product_data = validated_data.pop("products_id")
        user_data = validated_data.pop("user")

        # Cria a instância básica do pedido no banco de dados
        order = Order.objects.create(user=user_data)

        # Como é uma relação Many-to-Many, adicionamos cada produto individualmente ao pedido
        for product in product_data:
            order.product.add(product)
        # Retorna o pedido completo e populado
        return order
