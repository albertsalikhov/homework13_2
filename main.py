class Category:
    def __init__(self, name:str, description:str, products:list):
        self.name = name # название
        self.descriptions = description # описание
        self.categories = []  # общее количество категорий
        self.__products = products  # список продуктов

    def product_list(self, product):
        self.__products.append(product)
        return self.__products

    @property
    def products(self):
        products_str = []
        for product in self.__products:
            products_str.append(f'{product.name}, {product.price} руб. Остаток: {product.quantity_stock} шт.')
        return products_str



class Product:
    def __init__(self, name:str, descriptions:str, price:float, quantity_stock:int):
        self.name = name
        self.descriptions = descriptions
        self.price = price
        self.quantity_stock = quantity_stock


    @classmethod
    def products(cls, obj):
        name, price, quantity_stock = obj
        return cls(name, price, quantity_stock)

    @property
    def get_price(self):
        if self.price <=0:
            print('Цена введена некорректная')
        return self.price

    @get_price.setter
    def get_price(self, price):
        self.price = price





if __name__ == '__main__':
    product1 = Product('ноутбук', 'описание', '25000.00', 15)
    product2 = Product('телевизор', 'описание', '50000.00', 10)
    list_products = [product1, product2]
    category = Category('электроника', 'описание', list_products)
    category.product_list(list_products)
    print(Category.products)
