txt = input('Введите текст:')
print("Первый символ:", txt[0])
print("Последний символ:", txt[-1])
if len(txt) % 2 == 0:
    print("Среднего символа не существует.")
else:
    leng = int(len(txt))
    sr = leng // 2
    print ("Средний символ:", txt[sr])
