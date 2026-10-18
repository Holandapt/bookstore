import factory

from product.models import Product
from product.models import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    slug = factory.Faker("pystr")
    description = factory.Faker("pystr")
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker("pyint")
    title = factory.Faker("pystr")

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            # Se você passar categorias específicas ao chamar a factory, adiciona elas
            for category in extracted:
                self.category.add(category)
        else:
            # Se não passar nada, cria e adiciona uma categoria padrão automaticamente
            self.category.add(CategoryFactory())

    class Meta:
        model = Product
        skip_postgeneration_save = True
