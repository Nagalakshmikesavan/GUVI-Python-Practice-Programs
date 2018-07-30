n=int(input())
c=0
l=[]
lis=[]
for i in range(1,n+1):
	if n%i==0:
		l.append(i)
for i in l:
	if(i%2==0):
		lis.append(i)
print(*(lis))
	
