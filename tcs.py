n=int(input())
if(n%2==0):
	f=1

else:
	f=0
if f==0:
	n=int((n+1)/2)
	a=0
	b=1
	c=0
	for i in range(1,n+1):
		c=a+b
		a=b
		b=c
	print(a)
		
else:
	n=int(n/2)
	l=[]
	for i in range(2,100):
		for j in range(2,i):
			if(i%j==0):
				f=1
				break
		else:
			l.append(i)
	print(l[n-1])
	

		
