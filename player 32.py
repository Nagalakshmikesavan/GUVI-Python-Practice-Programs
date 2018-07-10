n,k=map(int,input().split())
l=[]
for i in range(0,n):
	inp=int(input())
	l.append(inp)
a=sorted(l)
if k in a:
	print("yes")
else:
	print("no")
