n,k=map(int,input().split())
n=map(int,input().split())
a=set(n)
k=map(int,input().split())
b=set(k)
if b.issubset(a):
	print("YES")
else:
	print("NO")
