n=int(input())
l=[]
m=input().split()
for i in range(0,n,2):
	if int(m[i])%2!=0:
		l.append(m[i])
for i in range(1,n,2):
	if int(m[i])%2==0:
		l.append(m[i])
print(*(l))
