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
def prod1():
    return Product('ноутбук', 'описание', 25000.00, 15)


@pytest.fixture()
def prod2():
    return Product('телефон', 'описание', 37000.00, 27)


def test_prod(prod1):
    assert prod1.name == 'ноутбук'
    assert prod1.descriptions == 'описание'
    assert prod1.price == 25000.00
    assert prod1.quantity_stock == 15


def test_prod_2(prod2):
    assert prod2.name == 'телефон'
    assert prod2.descriptions == 'описание'
    assert prod2.price == 37000.00
    assert prod2.quantity_stock == 27


def test_str(prod1):
    assert f'{prod1.name}, {prod1.price} руб. Остаток: {prod1.quantity_stock} шт.' == 'ноутбук, 25000.0 руб. Остаток: 15 шт.'


def test_add(prod1, prod2):
    assert prod1 + prod2 == 1374000.0

