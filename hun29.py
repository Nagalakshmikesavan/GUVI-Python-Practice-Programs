n=int(input())
a=input().split()
l=[]

for i in range(0,n):
	a[i]=int(a[i])
	l.append(a[i])
a=l[0]
for i in range(1,n):
	a=a+l[i]
print(a)
