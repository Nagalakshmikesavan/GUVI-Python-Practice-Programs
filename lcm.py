n=input()
m=n.split(" ")
a=int(m[0])
b=int(m[1])
c=a*b
if(a>b):
	greater_num=a
else:
	greater_num=b
lcm=greater_num
multiplier=1
while(lcm<c):
	if(lcm%a==0) and (lcm%b==0):
	
		break
	else:
		multiplier+=1
		lcm=multiplier*greater_num
print(lcm)
	
