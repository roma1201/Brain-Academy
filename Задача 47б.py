x=float(input('Введите число x:'))
y=float(input('Введите число y:'))
z=float(input('Введите число z:'))
if (x + y > z) and (x + z > y) and (y + z > x):
    print('Остроугольный')
else:
    print('Не остроугольный')
