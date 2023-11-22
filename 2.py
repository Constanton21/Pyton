number=int(input("Введите трехзначное число "))
a=number%10
b=int(number/10%10)
c=int(number/100%10)
print(c)
print (f"Сумма цифр = {a+b+c}")
print (f"What = {a+b+c}")