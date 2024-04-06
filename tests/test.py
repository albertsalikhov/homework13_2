import pytest

from pythonProject.src.classes import Category, Product, Smartphone, LawnGrass


@pytest.fixture()
def category():
    return Category('электроника', 'описание', ['ноутбук', 'описание', 25000.00, 15])


def test_category(category):
    assert category.name == 'электроника'
    assert category.descriptions == 'описание'
    assert category.total_number_of_categories == 1
    assert category.total_number_of_unique_products == 4


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
    assert (f'{prod1.name}, {prod1.price} руб. Остаток: {prod1.quantity_stock} шт.' ==
            'ноутбук, 25000.0 руб. Остаток: 15 шт.')


def test_add(prod1, prod2):
    assert prod1 + prod2 == 1374000.0


@pytest.fixture()
def prod3():
    return Smartphone('Iphone', 'описание', 65000.00, 13, 'Black',
                      '8Gb', '13 pro', '256Gb')


def test_prod3(prod3):
    assert prod3.name == 'Iphone'
    assert prod3.descriptions == 'описание'
    assert prod3.price == 65000
    assert prod3.quantity_stock == 13
    assert prod3.color == 'Black'
    assert prod3.performance == '8Gb'
    assert prod3.model == '13 pro'
    assert prod3.memory_capacity == '256Gb'


@pytest.fixture()
def prod4():
    return LawnGrass('Газон', 'описание', 2000, 43, 'green',
                     'Holland', '14 суток')


def test_prod4(prod4):
    assert prod4.name == 'Газон'
    assert prod4.descriptions == 'описание'
    assert prod4.price == 2000
    assert prod4.quantity_stock == 43
    assert prod4.color == 'green'
    assert prod4.manuf_country == 'Holland'
    assert prod4.germination_period == '14 суток'


def test_add_fails_without_info(prod2, prod3):
    with pytest.raises(TypeError):
        assert prod2 + prod3


@pytest.fixture()
def prod5():
    return Smartphone('Iphone', 'описание', 90000, 0, 'Grey',
                      '16Gb', '15 pro', '256Gb')


def test_prod5(prod5):
    assert prod5.name == 'Iphone'
    assert prod5.descriptions == 'описание'
    assert prod5.price == 90000
    assert prod5.quantity_stock == 0
    assert prod5.color == 'Grey'
    assert prod5.performance == '16Gb'
    assert prod5.model == '15 pro'
    assert prod5.memory_capacity == '256Gb'
