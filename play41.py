m,n=map(int,input().split())
l=[]
c=n
for i in range(0,1000):
	c=c*n
	l.append(c)
if m in l:
	print('yes')
else:
	print('no')
