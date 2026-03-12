# Читаем строку из файла
s = open("data.txt").readline()

current_length = 0  # Текущая длина правильной цепочки
max_length = 0  # Рекордная длина
next_expected_char = 'X'  # Символ, который мы ждем следующим

for char in s:
    # Если пришел именно тот символ, который мы ждали
    if char == next_expected_char:
        current_length += 1
        max_length = max(max_length, current_length)

        # Определяем, какой символ будет следующим в очереди
        if char == 'X':
            next_expected_char = 'Y'
        elif char == 'Y':
            next_expected_char = 'Z'
        else:  # если char == 'Z'
            next_expected_char = 'X'

    # Если пришел не тот символ, но это 'X' — начинаем новую цепочку с него
    elif char == 'X':
        current_length = 1
        next_expected_char = 'Y'

    # Если пришел не тот символ и это не 'X' — всё сбрасывается
    else:
        current_length = 0
        next_expected_char = 'X'

print(max_length)