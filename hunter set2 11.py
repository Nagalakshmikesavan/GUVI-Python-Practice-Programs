n=input()
m=n.split()
l=[]
for i in range(len(m)):
	a=m[i][::-1]
	l.append(a)
print(" ".join(l))
