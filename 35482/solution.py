lines = open('data.txt').readlines()
g_counts = []

# Считаем количество 'G' в каждой строке
for line in lines:
    count_g = line.count('G')
    g_counts.append(count_g)

# Находим строку, где 'G' меньше всего
# (используем индекс минимального значения из нашего списка счетчиков)
target_line = lines[g_counts.index(min(g_counts))]

char_frequency = {}

# Считаем, сколько раз встречается каждый символ в выбранной строке
for char in target_line:
    if char not in char_frequency:
        char_frequency[char] = 0
    char_frequency[char] += 1

# Выводим символ, который встречается чаще всего
print(max(char_frequency, key=char_frequency.get))