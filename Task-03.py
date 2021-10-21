# Задача 3. Клетки

n = int(input('Кол-во клеток: '))
n_list = []
unsuitable_list = []

for i in range(n):
    n_list.append(int(input(f'Эффективность {i + 1} клетки: ')))

for i in range(n):
    if n_list[i] < i:
        unsuitable_list.append(n_list[i])

print('\nНеподходящие значения:', end=' ')

for i in unsuitable_list:
    print(i, end=' ')
