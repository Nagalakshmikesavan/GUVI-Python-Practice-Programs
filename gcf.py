n=input()
m=n.split(" ")
a=int(m[0])
b=int(m[1])
if(a<b):
	smallest_num=a
else:
	smallest_num=b
gcf=smallest_num
for i in range(1,gcf+1):
	if(a%i==0) and (b%i==0):
		gcf=i
print(gcf)
