import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + '!@#$%^&'
    password = ''.join(random.choice(characters) for i in range(length))
    return password

while True:
    user_input = input('Enter length of password(Например, 12):')

    try:
        length = int(user_input)
        break
    except ValueError:
        print('Error! Please, enter only number, and not text. ')
        print('Try another')

print(f'Отлично, генерирую пароль длиной {length}....')

new_password = generate_password(length)
print(f'Your password: {new_password}')

with open('passwords.txt', 'a', encoding='utf-8') as file:
    file.write(new_password + '\n')

print('Пароль сохранен в файл passwords.txt!')




