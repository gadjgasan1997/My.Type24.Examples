# Читаем строку из файла
text_data = open('data.txt').readline()

max_length = -1  # Рекордная длина подходящего фрагмента
current_length = 0  # Длина текущего фрагмента между 'A'
e_in_current_segment = 0  # Счетчик букв 'E' в текущем фрагменте

for char in text_data:
    # Если встретили разделитель 'A'
    if char == 'A':
        # Проверяем: было ли в закончившемся фрагменте хотя бы три 'E'?
        if e_in_current_segment >= 3:
            max_length = max(max_length, current_length)

        # Обнуляем счетчики для начала нового фрагмента после 'A'
        e_in_current_segment = 0
        current_length = 0

    # Если встретили букву 'E'
    elif char == 'E':
        e_in_current_segment += 1
        current_length += 1

    # Если встретили любой другой символ (не 'A' и не 'E')
    else:
        current_length += 1

# Финальная проверка на случай, если последний фрагмент в файле тоже подходит
if e_in_current_segment >= 3:
    max_length = max(max_length, current_length)

print(max_length)