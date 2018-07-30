def arrays():
	n,k=map(int,input().split())
	l=[]
	r=[]
	for i in range(n):
		for j in range(k):
			r.append(int(input()))
		l.append(r)
		r=[]
	for i in range(n):
		for j in range(k):
			for a in range(i+1,n):
				for b in range(k):
					if l[i][j]==l[a][b]:
						print(l[i][j])
try:
	arrays()
except:
	print("invalid")
