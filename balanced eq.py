n=input()
c1=0
c2=0
for i in n:
	if i=='(':
		c1+=1
		
	if i==')':
		c2+=1
	
if c1==c2:
	print('YEs')
else:
	print('no')
