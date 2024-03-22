from pythonProject.src.classes import Product, Category

product1 = Product('ноутбук', 'описание', 25000.00, 15)
product2 = Product('телевизор', 'описание', 50000.00, 10)
list_products = [product1, product2]
category1 = Category('электроника', 'описание', list_products)
print(category1.product)
print(Category.total_number_of_categories)
print(product1)
print(category1)
print(product1 + product2)
print(len(category1))
print(category1.descriptions)



