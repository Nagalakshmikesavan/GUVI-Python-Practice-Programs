n=int(input())
m=input()
a=m.split(" ")
list=a
l=[]
for i in range(len(list)):
	if i==int(list[i]):
		l.append(list[i])
if(len(l)==0):
	print("-1")
else:
	print(" ".join(l))
