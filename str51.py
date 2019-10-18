a = input('Первая строка: ')
b = input('Вторая строка: ')
if set(b).difference(a):
    print('Нельзя')
else:
    print('Можно')
