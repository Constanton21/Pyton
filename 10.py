from random import randint

n=int(input("Введите число монеток "))
count0 =0
count1 =0
for i in range(n):
    mon = randint(0,1)
    print (mon, end=" ")
    if mon ==1:
        count1 +=1
    else:
        count0 +=1
if count1 < count0:
    print ('\n',count1)
else:
    print  ('\n',count0)