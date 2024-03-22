import pytest

from pythonProject.src.main import Category, Product


@pytest.fixture()
def category():
    return Category('электроника', 'описание', ['ноутбук', 'описание', 25000.00, 15])

def test_category(category):
    assert category.name == 'электроника'
    assert category.descriptions == 'описание'
    assert category.total_number_of_categories == 2
    assert category.total_number_of_unique_products == 6

@pytest.fixture()
def prod():
    return Product('ноутбук', 'описание', 25000.00, 15)

def test_prod(prod):
    assert prod.name == 'ноутбук'
    assert prod.descriptions == 'описание'
    assert prod.price == 25000.00
    assert prod.quantity_stock == 15

