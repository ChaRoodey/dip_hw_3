or_list = [int(i) for i in input('Введите список через пробел: ').split()]
rez_list = []

for i in or_list:
    if or_list.count(i) > 1 and i not in rez_list:
        rez_list.append(i)

print(f'Список дубликатов: {rez_list}')