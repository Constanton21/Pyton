s=int(input("Введите сумму двух чисел "))
p=int(input("Введите произведение чисел "))
x=1
while x<=1000:
    if x*x-s*x+p==0:
        y=s-x
        print (x, y)
        break
    else:
        x+=1
    if x==1001:
        print ("Данные некорректны")

