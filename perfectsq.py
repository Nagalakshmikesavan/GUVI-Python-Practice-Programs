n,m=map(int,input().split())
c=0
l=[]
for i in range(0,10000):
	a=i**2
	l.append(a)
for j in range(n,m+1):
	if j in l:
		c=c+1
print(c)
		
