x=int(input('Введите X:'))
y=int(input('Введите Y:'))
if x==y:
    print('Равенство')
elif x<y:
    print('Max.y=',y)
else:
        print('Max.x=',x)
#Или так
print(max(x,y))
