# Читаем одну строку из файла
s = open('data.txt').readline()

# Переменные для хранения рекорда
max_occurrences = 0
best_following_char = ''

# Перебираем все заглавные латинские буквы
for current_char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    # Считаем, сколько раз в тексте встречается комбинация 'A' + текущая буква
    pair_to_find = 'A' + current_char
    current_pair_count = s.count(pair_to_find)

    # Если нашли новую самую частую пару
    if current_pair_count > max_occurrences:
        max_occurrences = current_pair_count
        best_following_char = current_char

# Выводим букву, которая чаще всего была "соседом" буквы А справа
print(best_following_char)