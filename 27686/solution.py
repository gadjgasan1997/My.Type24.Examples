f = open('data.txt')
s = f.read()
s1 = 'X'
while s1 in s:
	s1 += 'X'
print(len(s1) - 1)