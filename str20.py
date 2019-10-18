a = input('Первое слово: ')
b = input('Второе слово: ')
z= a + b
for i in set(z):
    if z.count(i) == 2:
        print(i)
