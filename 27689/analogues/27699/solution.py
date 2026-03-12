# Читаем строку из файла
s = open("data.txt").readline()

current_length = 0  # Текущая длина правильной цепочки
max_length = 0  # Рекордная длина
next_expected_char = 'L'  # Символ, который мы ждем следующим

for char in s:
    # Если пришел именно тот символ, который мы ждали
    if char == next_expected_char:
        current_length += 1
        max_length = max(max_length, current_length)

        # Определяем, какой символ будет следующим в очереди
        if char == 'L':
            next_expected_char = 'D'
        elif char == 'D':
            next_expected_char = 'R'
        else:  # если char == 'R'
            next_expected_char = 'L'

    # Если пришел не тот символ, но это 'L' — начинаем новую цепочку с него
    elif char == 'L':
        current_length = 1
        next_expected_char = 'D'

    # Если пришел не тот символ и это не 'L' — всё сбрасывается
    else:
        current_length = 0
        next_expected_char = 'L'

print(max_length)