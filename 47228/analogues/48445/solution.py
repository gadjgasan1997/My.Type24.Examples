# Функции-помощники для проверки типа буквы
def is_consonant(symbol):
    # Возвращает True, если буква — согласная из набора C, D, F
    return symbol in 'CDF'

def is_vowel(symbol):
    # Возвращает True, если буква — гласная из набора A, O
    return symbol in 'AO'

# Читаем всё содержимое файла
full_text = open('data.txt').read()

max_streak = 0       # Рекордное количество цепочек подряд
current_streak = 0   # Текущее количество цепочек подряд
i = 0                # Индекс для обхода строки

# Идем по строке до предпредпоследнего символа (чтобы s[i+3] не выдал ошибку)
# Цикл for не поляет менять значение i руками внутри самого цикла
while i < len(full_text) - 2:

    # Если текущий символ — согласная, следующий — согласная и последний - гласная
    if is_consonant(full_text[i]) and is_consonant(full_text[i + 1]) and is_vowel(full_text[i + 2]):
        current_streak += 1

        # Обновляем рекорд
        max_streak = max(max_streak, current_streak)

        # Прыгаем через 3 символа (всю цепочку целиком)
        i += 3
    else:
        # Если цепочка не сложилась, обнуляем текущую серию
        current_streak = 0

        # Сдвигаемся на 1 символ вперед
        i += 1

# Печатаем максимальное число найденных цепочек
print(max_streak)