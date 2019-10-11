import math
#Правильное значение угла А
while True:
    try:
        a1=float(input('Угол А: '))
    except ValueError:
        print('Неверное значение')
        continue
    if a1<0:
        print('Неверное значение')
        continue
    if a1==0:
        print('Неверное значение')
        continue
    if a1==180:
        print('Неверное значение')
        continue
    if a1>180:
        print('Неверное значение')
        continue
    else:
        break
#Правильное значение угла В
while True:
    try:
        b1=float(input('Угол В: '))
    except ValueError:
        print('Неверное значение')
        continue
    if b1<0:
        print('Неверное значение')
        continue
    if b1==0:
        print('Неверное значение')
        continue
    if b1==180:
        print('Неверное значение')
        continue
    if b1>180:
        print('Неверное значение')
        continue
    if a1+b1>180:
        print('Неверное значение')
        continue
    if a1+b1==180:
        print('Неверное значение')
        continue
    else:
        break
#Прваильное значение угла С
#while True:
#    try:
#        c1=float(input('Угол C: '))
#    except ValueError:
#        print('Неверное значение')
#        continue
#    if c1<0:
#        print('Неверное значение')
#        continue
#    if c1==0:
#        print('Неверное значение')
#        continue
#    if c1==180:
#        print('Неверное значение')
#        continue
#    if c1>180:
#        print('Неверное значение')
#        continue
#    if a1+b1+c1>180:
#        print('Неверное значение')
#        continue
#    if a1+b1+c1<180:
#        print('Неверное значение')
#        continue
#    else:
#        break

#Автоматический просчёт угла С
c1=180-(a1+b1)
print('Угол C:',c1)
#Правильное значение Радиуса описанной окружности    
while True:
    try:
        r=float(input('Радиус описанной окружности: '))
    except ValueError:
        print('Неверное значение')
        continue
    if c1<0:
        print('Неверное значение')
        continue
    if c1==0:
        print('Неверное значение')
        continue
    else:
        break
        
a=2*r*math.sin(a1)
b=2*r*math.sin(b1)
c=2*r*math.sin(c1)

print('сторона А=:',a)
print('сторона B=:',b)
print('сторона C=:',c)
