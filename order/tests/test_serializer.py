import pytest

from order.serializers.order_serializers import OrderSerializer


# This test verifies wheter valid data is accepted:
@pytest.mark.django_db
def test_order_serializer_valid_data(valid_order_data):
    serializer = OrderSerializer(data=valid_order_data)
    assert serializer.is_valid(), serializer.errors


# This test verifies whetes mandatory fields are validated:
@pytest.mark.django_db
def test_serializer_requires_product(valid_order_data):
    valid_order_data.pop("products_id")
    serializer = OrderSerializer(data=valid_order_data)
    assert not serializer.is_valid()
    assert "products_id" in serializer.errors


# This test verifies the data produced by the serializer:
@pytest.mark.django_db
def test_serializer_return_expected_fields(default_order, default_product):
    serializer = OrderSerializer(default_order)
    assert serializer.data["user"] == 1
    assert serializer.data["total"] == default_product.price
