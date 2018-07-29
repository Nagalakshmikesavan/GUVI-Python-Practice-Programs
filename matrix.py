n=int(input())
m=int(input())
l=[]
lis=[]
for i in range(0,n):
	for j in range(0,m):
		inp=int(input())
		lis.append(inp)
	l.append(lis)
	lis=[]
for i in range(0,n):
	for j in range(0,m):
		if l[i][j]==0:
			lis.append([i,j])
for i,j in lis:
	for row in range(0,m):
		l[i][row]=0
	for col in range(0,n):
		l[col][j]=0
for j in range(m):
		print((l[j]))
