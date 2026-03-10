f = open("data.txt").readline()
k = 0
m = 0
expected = 'A'
for c in f:
	if c == expected:
		k += 1
		m = max(m, k)

		if c == 'X':
			expected = 'Y'
		elif c == 'Y':
			expected = 'Z'
		else:
			expected = 'X'
	elif c == 'X':
		expected = 'Y'
		k = 1
	else:
		expected = 'X'
		k = 0
print(m)