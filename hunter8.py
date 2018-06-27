n=int(input())
l=[]
for i in range(n):
	l.append(int(input()))
for i in range(0,len(l)):
	print(i)
	for k in range(i+1,len(l)):
		print(k)
		for j in range(k+1,len(l)):
			print(j)
			if (l[i]+l[k]==l[j]):
				print(l[i],l[k],l[j])
	
