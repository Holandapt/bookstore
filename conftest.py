import pytest

from product.factories import ProductFactory, CategoryFactory
from order.factories import OrderFactory, UserFactory


# We prepared the test scenarios:
@pytest.fixture
def default_product():
    return ProductFactory(
        title="Notebook",
        price=180,
    )


@pytest.fixture
def default_category():
    return CategoryFactory(title="Tecnologia")


@pytest.fixture
def valid_product_data(default_category):
    return {
        "title": "Notebook Dell",
        "price": 4500,
        "slug": "notebook-gamer",
        "categories_id": [default_category.id],
    }


# Fixtures for Order


@pytest.fixture
def default_user():
    return UserFactory(username="fakeUsername", email="fakeEmail")


@pytest.fixture
def default_order(default_user, default_product):
    return OrderFactory(user=default_user, product=[default_product])


@pytest.fixture
def valid_order_data(default_user, default_product):
    return {
        "user": default_user.id,
        "products_id": [default_product.id],
    }
