class Category:
    total_number_of_categories = 0
    total_number_of_unique_products = 0

    def __init__(self, name:str, description:str, products:list):
        self.name = name # название категории
        self.descriptions = description # описание категории
        self.__products = products  # список продуктов
        Category.total_number_of_categories += 1  # общее количество категорий
        Category.total_number_of_unique_products += len(self.__products)

    def add_products(self, *args):
        self.__products.append(args)


    @property
    def products(self):
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
    def __init__(self, name:str, descriptions:str, price:float, quantity_stock:int):
        self.name = name
        self.descriptions = descriptions
        self.price = price
        self.quantity_stock = quantity_stock


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
        result = (self.price * self.quantity_stock) + (other.price * other.quantity_stock)
        return result





if __name__ == '__main__':
    product1 = Product('ноутбук', 'описание', 25000.00, 15)
    product2 = Product('телевизор', 'описание', 50000.00, 10)
    list_products = [product1, product2]
    category1 = Category('электроника', 'описание', list_products)
    print(category1.products)
    print(Category.total_number_of_categories)
    print(product1)
    print(category1)
    print(product1 + product2)
    print(len(category1))

