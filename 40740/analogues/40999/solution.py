# Читаем строку из файла
text_data = open('data.txt').readline()

max_length = -1  # Рекордная длина подходящего фрагмента
current_length = 0  # Длина текущего фрагмента между 'E'
e_in_current_segment = 0  # Счетчик букв 'A' в текущем фрагменте

for char in text_data:
    # Если встретили разделитель 'E'
    if char == 'E':
        # Проверяем: было ли в закончившемся фрагменте хотя бы три 'A'?
        if e_in_current_segment >= 3:
            max_length = max(max_length, current_length)

        # Обнуляем счетчики для начала нового фрагмента после 'E'
        e_in_current_segment = 0
        current_length = 0

    # Если встретили букву 'A'
    elif char == 'A':
        e_in_current_segment += 1
        current_length += 1

    # Если встретили любой другой символ (не 'E' и не 'A')
    else:
        current_length += 1

# Финальная проверка на случай, если последний фрагмент в файле тоже подходит
if e_in_current_segment >= 3:
    max_length = max(max_length, current_length)

print(max_length)