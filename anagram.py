word=sorted('kabali')
n=int(input())
list=[]
c=0
for i in range(0,n):
	m=input()
	list.append(m)
for i in list:
	if word==sorted(i):
		c=c+1
print(c)
