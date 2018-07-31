n=int(input())
l=[]
m=input().split()
for i in range(n):
	if i%2==0 and  int(m[i])%2!=0:
		l.append(m[i])
	elif i%2!=0 and int(m[i])%2==0:
		l.append(m[i])
	
print(*(l))
