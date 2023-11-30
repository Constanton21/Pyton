import random

list_1 = [random.randint(1, 5) for _ in range(10)]
k = int(input("Введите искомое значение k: "))
count = 0
for _ in list_1:
    if _ == k:
        count += 1
print(count)
# print(f"Число {k} в массиве {list_1} встречается  {count} раз(а).")