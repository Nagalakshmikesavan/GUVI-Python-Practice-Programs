try:
	n=int(input())
	l=[]
	li=[]
	m=input().split()
	for i in range(0,n):
		c=0
		for j in range(0,n):
			if(m[i]==m[j]):
				c=c+1
		if c>1:
			l.append(m[i])
	print(l[0])
except:
	print('unique')
	
