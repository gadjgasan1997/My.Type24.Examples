f = open("data.txt").readline()
k = 0
m = 0
expected = 'A'
for c in f:
	if c == expected:
		k += 1
		m = max(m, k)

		if c == 'A':
			expected = 'B'
		else:
			expected = 'A'
	elif c == 'A':
		expected = 'B'
		k = 1
	else:
		expected = 'A'
		k = 0
print(m)