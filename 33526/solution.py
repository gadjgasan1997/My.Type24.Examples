# Читаем всё содержимое файла в одну строку
s = open('data.txt').read()

# Словарь для хранения частоты букв, стоящих между одинаковыми символами
middle_char_counts = {}

# Идем по строке до предпредпоследнего символа, чтобы не выйти за границы [i+2]
for i in range(len(s) - 2):
    # Если крайние символы тройки совпадают (например, 'A X A')
    if s[i] == s[i+2]:
        # Берем символ, который стоит посередине
        middle_char = s[i+1]

        # Увеличиваем счетчик для этого символа в словаре
        if middle_char in middle_char_counts:
            middle_char_counts[middle_char] += 1
        else:
            middle_char_counts[middle_char] = 1

# Находим ключ (символ) с максимальным значением в словаре
most_frequent_middle = max(middle_char_counts, key=middle_char_counts.get)

# Выводим букву, которая чаще всего стояла между одинаковыми
print(most_frequent_middle)