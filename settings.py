from faker import Faker

# Валидные тестовые данные для авторизации в системе:
valid_firstname = 'Ксения'
valid_lastname = 'Волкова'
valid_email = 'ksenia_volkova@inbox.ru'
valid_phone = '+79960266007'
valid_login = 'kessyname'
valid_ls = '111111111111'
valid_pass = 'wofmyg4dypjifoxDom'

# Невалидные и фейковые данные для авторизации в системе

# RUS кириллические символы
fake_ru = Faker('ru_RU')
fake_firstname = fake_ru.first_name()
fake_lastname = fake_ru.last_name()
fake_phone = fake_ru.phone_number()

# ENG латинские символы
fake = Faker()
fake_firstname_en = fake.first_name()
fake_lastname_en = fake.last_name()
fake_password = fake.password()
fake_email = fake.email()
fake_login = fake.user_name()

#Цифры
invalid_ls = '656565656565'
