import random, string

char = string.ascii_letters + string.digits + string.punctuation
pass_lenght = int(input('Введите длину пароля: '))

password = ''.join(random.choice(char) for i in range(pass_lenght))

print(f'Пароль: {password}')