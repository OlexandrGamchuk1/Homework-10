class Customer():
    def __init__(self, surname, name, patronymic, age, phone_number):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.age = age
        self.phone_number = phone_number

    def information(self):
        return f'Surname: {self.surname.title()}\nName: {self.name.title()}' \
               f'\nPatronymic: {self.patronymic.title()}\nAge: {str(self.age)}' \
               f'\nPhone number: +{self.phone_number}'


client = Customer('gamchuk', 'olexandr', 'vasylovych', 18, 380961224125)
print(client.information())