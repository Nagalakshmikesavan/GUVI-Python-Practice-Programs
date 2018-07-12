n=int(input())
m=int(input())
c=0
l=[]
for i in range(n,m+1):
	a=i**2
	l.append(a)
for j in range(n,m+1):
	if j in l:
		c=c+1
print(c)
