class Order():
    def __init__(self, surname, name, phone):
        self.surname = surname
        self.name = name
        self.phone = phone
        self.order = []
        self.summa = 0

    def product(self, product, price):
        self.order.append(product)
        self.summa += price

    def __str__(self):
        return f'\tOOO "Online store"\nSurname: {self.surname.title()}\nName: {self.name.title()}' \
               f'\nPhone: +{self.phone}\nOrder: {", ".join(self.order)}\nSum: {self.summa}₴'


customer = Order('gamchuk', 'olexandr', 380961224125)
customer.product('Nightstand', 4000)
customer.product('Refrigerator', 15000)
print(customer)