# Задача 1. Генерация списка

n = int(input("Введите число: "))
list_n = []

for n in range(1, n + 1, 2):
    list_n.append(n)

print(list_n)
