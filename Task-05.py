# Задача 5. Кино

def print_films(film_list):
    len_list = len(film_list)
    film_str = ''
    for i in range(len_list):
        film_str += str(film_list[i]) + ', '
    return film_str


def search_film(film, catalog):
    flag = False
    for i in catalog:
        if film == str(i):
            flag = True
            break
    return flag


ans = ''
favorites_film = []
films = [
    'Крепкий орешек',
    'Назад в будущее',
    'Таксист',
    'Леон',
    'Богемская рапсодия',
    'Город грехов',
    'Мементо', 'Отступники',
    'Деревня'
]

print("Фильмы, которые есть в фильмотеке:\n", print_films(films))
print('Введите название фильма, чтобы добавить его в избраное.\nДля выхода введите "0"')

while True:
    ans = input('Название фильма :')
    if ans == '0':
        break
    elif search_film(ans, films):
        favorites_film.append(ans)
    else:
        print('Ошибка. Такого фильма нет в фильмотеке. Попробуйте еще раз или введите "0" для выхода.')

print("Фильмы, которые вы добавили в избранное:\n", print_films(favorites_film))
