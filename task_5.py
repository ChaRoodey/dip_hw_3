first_word = input('Введите первое слово: ')
second_word = input('Введите второе слово: ')

if len(first_word) != len(second_word):
    print('Слова не анограммы')
    quit()

for i in range(len(second_word)):
    if second_word[i] not in first_word or first_word[i] not in second_word:
        print('Слова не являются анограммами')
        quit()

print('Слова являются анограммами')
