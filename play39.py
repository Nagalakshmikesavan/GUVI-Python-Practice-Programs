n=int(input())
l=[]
c=2
for i in range(0,1000):
	c=c*2
	l.append(c)
if n in l:
	print('yes')
else:
	print('no')
