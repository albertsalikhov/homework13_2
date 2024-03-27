class Category:
    total_number_of_categories = 0
    total_number_of_unique_products = 0

    def __init__(self, name:str, description:str, products:list):
        self.name = name # название категории
        self.descriptions = description # описание категории
        self.__products = products  # список продуктов
        Category.total_number_of_categories += 1  # общее количество категорий
        Category.total_number_of_unique_products += len(self.__products) # количество уникальных продуктов

    def add_products(self, *args):
        self.__products.append(args)


    @property
    def product(self):
        products_str = []
        for product in self.__products:
            products_str.append( f'{product.name}, {product.price} руб. Остаток: {product.quantity_stock} шт.')
        return products_str

    def __len__(self):
        general_products = 0
        for prod in self.__products:
            general_products += prod.quantity_stock
        return general_products

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'


class Product:
    def __init__(self, name:str, descriptions:str, price:float, quantity_stock:int, color=None):
        self.name = name
        self.descriptions = descriptions
        self.price = price
        self.quantity_stock = quantity_stock
        self.color = color

    @classmethod
    def products(cls, **obj):
        name, price, quantity_stock = obj
        return cls(name, price, quantity_stock)


    @property
    def get_price(self):
        return self.price

    @get_price.setter
    def get_price(self, price):
        if self.price <=0:
            print('Цена введена некорректная')
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity_stock} шт.'

    def __add__(self, other):
        if type(self) == type(other):
            result = (self.price * self.quantity_stock) + (other.price * other.quantity_stock)
            return result
        else:
            raise TypeError('Продукт не соответствует типу')


class Smartphone(Product):
    def __init__(self, name:str, descriptions:str, price:float, quantity_stock:int, color, performance, model, memory_capacity):
        super().__init__(name, descriptions, price, quantity_stock, color)
        self.performance = performance
        self.model = model
        self.memory_capacity = memory_capacity


class LawnGrass(Product):
    def __init__(self, name:str, descriptions:str, price:float, quantity_stock:int, color, manufacturer_country, germination_period):
        super().__init__(name, descriptions, price, quantity_stock, color)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period











