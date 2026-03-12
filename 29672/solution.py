# Открываем файл для чтения
s = open('data.txt')

# Счетчик строк, подходящих под наше условие
matching_lines_count = 0

# Перебираем файл построчно
for current_line in s:
    # Считаем количество букв 'A' и 'E' в текущей строке
    a_occurrences = current_line.count('A')
    e_occurrences = current_line.count('E')

    # Если 'A' встречается меньше раз, чем 'E'
    if a_occurrences < e_occurrences:
        matching_lines_count += 1

# Выводим итоговое количество строк
print(matching_lines_count)