n,k=map(int,input().split())
l=[]
n=map(int,input().split())
a=set(n)
l.append(max(a))
k=map(int,input().split())
b=set(k)
l.append(max(b))
ans=str(l)[1:-1]
print(ans.replace(',',''))

