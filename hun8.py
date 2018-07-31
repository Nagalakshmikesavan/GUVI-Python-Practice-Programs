n=int(input())
m=input().split()
for i in range(0,n):
	for j in range(i+1,n):
		for a in range(j+1,n):
			if int(m[i])+int(m[j])==int(m[a]):
				print(int(m[i]),int(m[j]),int(m[a]))
