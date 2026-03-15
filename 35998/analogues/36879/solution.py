# Читаем все строки из файла в список
all_lines = open('data.txt').readlines()
max_distance_found = 0

# Перебираем каждую строку по отдельности
for current_line in all_lines:
    # Условие: в строке должно быть меньше 25 букв 'G'
    if current_line.count('G') < 25:

        # Проверяем каждую букву латинского алфавита
        for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            # Если буква есть в строке хотя бы один раз
            if char in current_line:
                # Находим индекс первого появления (index) и последнего (rindex)
                first_pos = current_line.index(char)
                last_pos = current_line.rindex(char)

                # Считаем расстояние между ними и обновляем общий рекорд
                current_distance = last_pos - first_pos
                max_distance_found = max(max_distance_found, current_distance)

# Выводим самый большой найденный интервал
print(max_distance_found)