from pythonProject.src.classes import Product, Category, Smartphone, LawnGrass

product1 = Product('ноутбук', 'описание', 25000.00, 15)
product2 = Product('телевизор', 'описание', 50000.00, 10)
product3 = Smartphone('Iphone', 'описание ', 65000.00, 13, 'Black', '8Gb', '13 pro', '256Gb')
product4 = LawnGrass('Газон', 'описание', 2000, 43, 'green', 'Holland',
                 '14 суток')
list_products = [product1, product2, product3]
category1 = Category('электроника', 'описание', list_products)
print(category1.product)
print(Category.total_number_of_categories)
print(product3)
print(category1)
print(product1 + product2)
print(len(category1))
print(category1.descriptions)



