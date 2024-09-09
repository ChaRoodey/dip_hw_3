origin_str = input('Введите строку: ')

origin_str = origin_str.lower()
lenght_str = len(origin_str)

for i in range(lenght_str // 2):
    if origin_str[i] != origin_str[lenght_str - i - 1]:
        print('Строка не является палиндромом')
        quit()

print('Строка является палиндромом')
