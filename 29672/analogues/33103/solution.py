# Открываем файл для чтения
s = open('data.txt')

# Счетчик строк, подходящих под наше условие
matching_lines_count = 0

# Перебираем файл построчно
for current_line in s:
    # Считаем количество букв 'E' и 'A' в текущей строке
    e_occurrences = current_line.count('E')
    a_occurrences = current_line.count('A')

    # Если 'E' встречается меньше раз, чем 'A'
    if e_occurrences < a_occurrences:
        matching_lines_count += 1

# Выводим итоговое количество строк
print(matching_lines_count)