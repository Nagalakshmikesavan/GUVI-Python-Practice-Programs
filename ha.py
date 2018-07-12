n,k=map(int,input().split())
a=list(str(n))
c=0
for i in a:
	if int(i)==k:
		c=c+1
print(c)
