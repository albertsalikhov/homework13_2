from abc import ABC, abstractmethod


class Category:
    total_number_of_categories = 0
    total_number_of_unique_products = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name  # название категории
        self.descriptions = description  # описание категории
        self.__products = products  # список продуктов
        Category.total_number_of_categories += 1  # общее количество категорий
        Category.total_number_of_unique_products += len(self.__products)  # количество уникальных продуктов

    def add_products(self, *args):
        if isinstance(args, Product):
            self.__products.append(args)
        raise TypeError('Только Product и наследники Product')

    @property
    def product(self):
        products_str = []
        for product in self.__products:
            products_str.append(f'{product.name}, {product.price} руб. Остаток: {product.quantity_stock} шт.')
        return products_str

    def __len__(self):
        general_products = 0
        for prod in self.__products:
            general_products += prod.quantity_stock
        return general_products

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'


class Commodity(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def products(self):
        pass


class MixinLog:
    def __repr__(self):
        products = [f'{i}' for i in self.__dict__.values()]
        return f'Создан объект {self.__class__.__name__},{', '.join(products)}'


class Product(Commodity, MixinLog):
    def __init__(self, name: str, descriptions: str, price: float, quantity_stock: int):
        self.name = name
        self.descriptions = descriptions
        self.price = price
        self.quantity_stock = quantity_stock

    @classmethod
    def products(cls, **obj):
        name, descriptions, price, quantity_stock = obj
        return cls(name, descriptions, price, quantity_stock)

    @property
    def get_price(self):
        return self.price

    @get_price.setter
    def get_price(self, price):
        if self.price <= 0:
            print('Цена введена некорректная')
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity_stock} шт.'

    def __add__(self, other):
        if type(self) is type(other):
            result = (self.price * self.quantity_stock) + (other.price * other.quantity_stock)
            return result
        else:
            raise TypeError('Продукт не соответствует типу')


class Smartphone(Product, MixinLog):
    def __init__(self, name: str, descriptions: str, price: float, quantity_stock: int, color: str, performance: str,
                 model: str, memory_capacity: str):
        super().__init__(name, descriptions, price, quantity_stock)
        self.color = color
        self.performance = performance
        self.model = model
        self.memory_capacity = memory_capacity

    @classmethod
    def products(cls, **obj):
        name, descriptions, price, quantity_stock, color, performance, model, memory_capacity = obj
        return cls(name, descriptions, price, quantity_stock, color, performance, model, memory_capacity)


class LawnGrass(Product, MixinLog):
    def __init__(self, name: str, descriptions: str, price: float, quantity_stock: int, color: str, manuf_country: str,
                 germination_period: str):
        super().__init__(name, descriptions, price, quantity_stock)
        self.color = color
        self.manuf_country = manuf_country
        self.germination_period = germination_period

    @classmethod
    def products(cls, **obj):
        name, descriptions, price, quantity_stock, color, manuf_country, germination_period = obj
        return cls(name, descriptions, price, quantity_stock, color, manuf_country, germination_period)
