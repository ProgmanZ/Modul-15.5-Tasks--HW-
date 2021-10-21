# Задача 4. Видеокарты

def out_fun(list_models):
    models = '[ '
    for mdl in range(len(list_models)):
        models += str(list_models[mdl]) + ' '
    models += ' ]'
    return models


n_cards = int(input('Кол-во видеокарт: '))
old_list = []
new_list = []

for i in range(n_cards):
    old_list.append(int(input(f'{i + 1} Видеокарта: ')))

max_vol = old_list[0]

for i in range(n_cards):
    if old_list[i] > max_vol:
        max_vol = old_list[i]

for i in range(n_cards):
    if max_vol != old_list[i]:
        new_list.append(old_list[i])

print('\nСтарый список видеокарт:', out_fun(old_list))
print('Новый список видеокарт:', out_fun(new_list))
