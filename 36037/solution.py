# Читаем строку из файла
full_text = open('data.txt').readline()

# Разрезаем строку на части везде, где встречается комбинация 'XZZY'
# Сама комбинация 'XZZY' при этом исчезает из частей
fragments = full_text.split('XZZY')

max_segment_length = 0

# Перебираем все полученные кусочки
for i in range(len(fragments)):
    # Считаем длину текущего куска
    # Прибавляем 6, так как перед куском слева было ZZY, а справа XZZ
    # Такое проиходит, так как мы разделили строку по XZZY
    # Т.е., если была строка XZZYABCXZZY, то максимальное количество идущих подряд символов,
    # среди которых нет подстроки XZZY будет 9 (ZZY + ABC + XZZ)
    current_length = len(fragments[i]) + 6

    # Обновляем рекорд
    max_segment_length = max(current_length, max_segment_length)

# Выводим максимальный результат
print(max_segment_length)