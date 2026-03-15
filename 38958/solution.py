# Читаем одну строку из файла
full_text = open('data.txt').readline()

# Разрезаем текст по символу 'A'.
# В списке fragments окажутся части текста, в которых букв 'A' вообще нет.
fragments = full_text.split('A')

max_streak = 0

# Перебираем фрагменты по парам (текущий и следующий)
for i in range(len(fragments) - 1):
    # Длина левого куска без 'A'
    left_part_len = len(fragments[i])
    # Длина правого куска без 'A'
    right_part_len = len(fragments[i + 1])

    # Складываем длины двух соседних кусков и прибавляем 1 (саму букву 'A', которая была между ними)
    # Это дает нам длину самой длинной последовательности, содержащей ровно одну 'A'
    combined_length = left_part_len + right_part_len + 1

    # Обновляем рекорд
    max_streak = max(max_streak, combined_length)

# Печатаем итоговый результат
print(max_streak)