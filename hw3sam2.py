import random

list_1 = [random.randint(1, 20) for _ in range(5)]
k = int(input("Введите значение k: "))

bl_el = 0
min_razn = 100

for i in range(len(list_1)):
    razn = abs(list_1[i] - k)
    if razn < min_razn:
        min_razn = razn
        bl_el = list_1[i]
print(bl_el)
# print(f"Самый близкий элемент к числу {k} в массиве {list_1} - {bl_el}.")
