class Products():
    def __init__(self, product, height, width, weight, price):
        self.product = product
        self.height = height
        self.width = width
        self.weight = weight
        self.price = price

    def __str__(self):
        return f'Product: {self.product}\nHeight: {str(self.height)}mm\nWidth: {str(self.width)}mm' \
               f'\nWeight: {str(self.weight)}kg\nPrice: {str(self.price)}₴\n'


my_product = Products('Nightstand', 123, 60, 4, 4000)
print(my_product)
my_product = Products('Refrigerator', 224, 102, 20, 15000)
print(my_product)