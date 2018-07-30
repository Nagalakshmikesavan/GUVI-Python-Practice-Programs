n=int(input())
c=0
l=[]
for i in range(1,n):
	if n%i==0:
		l.append(i)
print(*(l))
	
