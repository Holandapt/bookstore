import pytest

from product.serializers import ProductSerializer


# This test verifies whether valid data is accepted:
@pytest.mark.django_db
def test_product_serializer_valid_data(valid_product_data):

    # Instancia o serializer passando os dados no parâmetro 'data' e verifica se os dados são válidos;
    serializer = ProductSerializer(data=valid_product_data)
    assert serializer.is_valid(), serializer.errors


# This test verifies whether mandatory fields are validated:
@pytest.mark.django_db
def test_serializer_requires_category(valid_product_data):
    # Remove o titulo para ver se é obrigatório.
    valid_product_data.pop("categories_id")
    serializer = ProductSerializer(data=valid_product_data)
    assert not serializer.is_valid()
    assert "categories_id" in serializer.errors


# This test verifies that invalid data are rejected:
@pytest.mark.django_db
def test_serializer_rejects_price_invalid(valid_product_data):
    valid_product_data["price"] = -1
    serializer = ProductSerializer(data=valid_product_data)
    assert not serializer.is_valid()
    assert "price" in serializer.errors


# This test verifies the data produced by the serializer:
@pytest.mark.django_db
def test_serializer_returns_expected_fields(default_product):
    serializer = ProductSerializer(default_product)
    expected_fields = {"id", "title", "price", "description", "active", "category"}
    assert expected_fields.issubset(set(serializer.data.keys()))


# This test validates whether the Serializer is converting correctly
# an instance of the database model in serialized data:
@pytest.mark.django_db
def test_product_serializer(default_product):
    # Instancia o serializer passando a instância do modelo
    serializer = ProductSerializer(instance=default_product)
    # 3. Verifica se os dados serializados correspondem ao esperado
    assert serializer.data["title"] == "Notebook"
    assert serializer.data["price"] == 180
