f = open('data.txt').readline()

current_streak = 1  # Текущая длина цепочки из разных символов
max_streak = 0      # Рекордная длина

# Перебираем строку со второго символа, чтобы сравнивать с предыдущим
for i in range(1, len(f)):
    # Если текущий символ НЕ такой же, как предыдущий
    if f[i] != f[i-1]:
        current_streak += 1
    else:
        # Если встретили дубль (например, 'AA'), фиксируем рекорд
        max_streak = max(max_streak, current_streak)
        # Сбрасываем счетчик (текущий символ уже образует новую цепочку длиной 1)
        current_streak = 1

# Финальная проверка рекорда (на случай, если самая длинная цепочка была в конце)
max_streak = max(max_streak, current_streak)

print(max_streak)