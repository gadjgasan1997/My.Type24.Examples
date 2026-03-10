f = open('data.txt')
s = f.read()
s1 = 'Y'
while s1 in s:
	s1 += 'Y'
print(len(s1) - 1)