# Читаем одну строку из файла
full_text = open('data.txt').readline()

# Разрезаем текст по символу 'D'.
# В списке fragments окажутся части текста, в которых букв 'D' вообще нет.
fragments = full_text.split('D')

max_streak = 0

# Перебираем фрагменты по парам (текущий и следующий)
for i in range(len(fragments) - 1):
    # Длина левого куска без 'D'
    left_part_len = len(fragments[i])
    # Длина правого куска без 'D'
    right_part_len = len(fragments[i + 1])

    # Складываем длины двух соседних кусков и прибавляем 1 (саму букву 'D', которая была между ними)
    # Это дает нам длину самой длинной последовательности, содержащей ровно одну 'D'
    combined_length = left_part_len + right_part_len + 1

    # Обновляем рекорд
    max_streak = max(max_streak, combined_length)

# Печатаем итоговый результат
print(max_streak)