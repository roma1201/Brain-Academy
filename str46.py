a=input('enter string: ').split()
count=0
a.sort(key=len, reverse=True)
a = ' '.join(a)
print('По убыванию: ', a)
