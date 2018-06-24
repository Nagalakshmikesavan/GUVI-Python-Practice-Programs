n=int(input())
m=input()
a=m.split(" ")
b=set(a)
for i in b:
	c=0
	for j in a:
		if(j==i):
			c=c+1
	if(c==1):
		print(i)
