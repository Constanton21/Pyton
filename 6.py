number=int(input("Введите номер билета(6 цифр) "))
num1=int(number/1000)
num2=int(number%1000)
sum1=int(num1/100%10)+int(num1/10%10)+int(num1%10)
sum2=int(num2/100%10)+int(num2/10%10)+int(num2%10)
if sum1==sum2:
    print("счастливый билет")
else: 
    print("несчастливый билет")
