winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

month = int(input ("введите номер месяца от 1 до 12 "))

if month in winter:
    print ("это зимний месяц")
elif month in spring:
    print ("это весенний месяц")
elif month in summer:
    print ("это летний месяц")
elif month in autumn:
    print ("это осенний месяц")
else:
    print ("введено некорректное число")
