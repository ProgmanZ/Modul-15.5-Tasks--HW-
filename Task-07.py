# Задача 7. Контейнеры

def weight_input(dialog):
    while True:
        print(dialog, end='')
        weight_container = int(input())
        if 200 >= weight_container > 0:
            break
        else:
            print("Ошибка. Вес контейнера не может превышать 200 кг.")
    return weight_container


def search_place(weight_new_container, container_list):
    count = 0
    for numb_cont in range(len(container_list)):
        if weight_new_container > container_list[numb_cont]:
            count += 1
            break
        count += 1
    return count


containers = int(input("Кол-во контейнеров: "))
data_containers = []
old_dialog = 'Введите вес контейнера (кг): '
new_dialog = 'Введите вес нового контейнера (кг): '

for container in range(containers):
    data_containers.append(weight_input(old_dialog))

new_container = weight_input(new_dialog)
numb = search_place(new_container, data_containers)
<<<<<<< HEAD

=======
>>>>>>> origin/main
print('Номер, куда встанет новый контейнер: ', numb)
