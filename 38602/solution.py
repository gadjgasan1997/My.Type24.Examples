# Читаем одну строку из файла
text_data = open('data.txt').readline()

max_streak = 0  # Рекордная длина цепочки
current_streak = 0  # Длина текущей цепочки
previous_char = ''  # Переменная для хранения предыдущего символа

for current_char in text_data:
    # Проверяем условие разрыва: если текущий и предыдущий символы — оба 'P'
    if previous_char == 'P' and current_char == 'P':
        # Фиксируем достигнутый результат в рекорды
        max_streak = max(max_streak, current_streak)
        # Начинаем новую цепочку с текущей буквы 'P' (её длина 1)
        current_streak = 1
    else:
        # В любом другом случае (если это не 'PP') цепочка продолжается
        current_streak += 1

    # Сохраняем текущий символ как "предыдущий" для следующего шага цикла
    previous_char = current_char

# Финальная проверка на случай, если самая длинная цепочка была в конце файла
max_streak = max(max_streak, current_streak)

print(max_streak)