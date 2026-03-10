f=open('data.txt')
s=f.read()
s1='A'
while s1 in s:
	s1+='A'
print(len(s1) - 1)