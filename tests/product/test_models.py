import pytest

from tests.factories import CategoryFactory, BrandFactory, ProductFactory

pytestmark = pytest.mark.django_db


class TestCategoryModels:
    def test_string_method(self, category_factory):
        obj = category_factory(name='test_category')
        assert obj.__str__() == 'test_category'


class TestBrandModels:
    def test_string_method(self, brand_factory):
        obj = brand_factory(name='test_brand')
        assert obj.__str__() == 'test_brand'


class TestProductModels:
    def test_string_method(self, product_factory):
        obj = product_factory(name='test_product')
        assert obj.__str__() == 'test_product'
