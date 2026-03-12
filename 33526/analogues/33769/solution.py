# Загружаем содержимое файла
s = open('data.txt').read()

# Словарь для подсчета символов, идущих после пары одинаковых
char_after_double_counts = {}

# Начинаем с 2, чтобы s[i-2] всегда указывал на существующий символ в начале
for i in range(2, len(s)):
    # Если два предыдущих символа одинаковы (например, 'AA X')
    if s[i-1] == s[i-2]:
        # Нас интересует текущий символ, который стоит сразу за парой
        target_char = s[i]

        # Обновляем количество встреч этого символа
        if target_char in char_after_double_counts:
            char_after_double_counts[target_char] += 1
        else:
            char_after_double_counts[target_char] = 1

# Определяем символ, который чаще всего шел после дублей
most_common_char = max(char_after_double_counts, key=char_after_double_counts.get)

print(most_common_char)