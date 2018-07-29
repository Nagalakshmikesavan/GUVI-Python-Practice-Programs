n=int(input())
l=[]
op=[]
for i in range(0,n):
	inp=int(input())
	l.append(inp)
	op.append(1)
for i in range(0,n):
	for j in range(0,n):
		if l[i]!=l[j]:
			op[i]*=l[j]
print(*(op))
