n=int(input())
c=0
l=[[x for x in range(n)] for j in range(n)]
for i in range(0,n):
	for j in range(0,n):
		l[i][j]=int(input())
for i in range(0,n):
	for j in range(1,n-1):
		if i==0 and l[i][j-1]==0 and l[i][j+1]==0 and l[i+1][j]==0:
			c=c+1
		elif i==n-1 and l[i][j-1]==0 and l[i][j+1]==0 and l[i-1][j]==0:
			c=c+1
		elif i!=0 and i!=n-1 and  l[i][j+1]==0 and l[i][j-1]==0 and l[i+1][j]==0 and l[i-1][j]==0:
			c=c+1
print(c)
		
