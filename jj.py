n=input()
l=[]
list=[]
l=n.split()
n=int(l[0])
k=int(l[1])
m=input()
inp=m.split()

for i in range(len(inp)):
	if k==int(i):
		print('yes')
if k is not int(i):
	print('no')
