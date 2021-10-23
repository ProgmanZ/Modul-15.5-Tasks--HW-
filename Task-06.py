# Задача 6. Анализ слова

word = list(input("Введите слово: "))
word_length = len(word)
count = word_length * 2

for i in range(word_length):
    for j in range(word_length):
        if str(word[i]) == str(word[j]):
            count -= 1

print("Кол-во уникальных букв:", count)
