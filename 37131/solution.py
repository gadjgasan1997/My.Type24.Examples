# Читаем одну строку из файла
full_text = open('data.txt').readline()

# Чтобы цепочки из букв K и L разорвались, вставляем между ними пробел
# 'KL' превращается в 'K L', 'LK' превращается в 'L K'
text_with_separators = full_text.replace('KL', 'K L')
text_with_separators = text_with_separators.replace('LK', 'L K')

# Разрезаем текст по пробелам на список отдельных фрагментов (частей)
# Теперь в каждой части гарантированно нет запрещенных сочетаний
fragments = text_with_separators.split(' ')

max_length = 0

# Перебираем все полученные фрагменты
for current_fragment in fragments:
    # Считаем длину текущего фрагмента
    current_length = len(current_fragment)

    # Если текущий фрагмент длиннее нашего рекорда — обновляем максимум
    if current_length > max_length:
        max_length = current_length

# Выводим самую большую найденную длину
print(max_length)