ab=input()
sp1=ab.split(" ")
a=sp1[0]
b=sp1[1]
mn=input()
sp2=mn.split(" ")
m=sp2[0]
n=sp2[1]
xy=input()
sp3=xy.split(" ")
x=sp3[0]
y=sp3[1]
d=(int(n)-int(b))*(int(x)-int(m))
f=(int(y)-int(n))*(int(m)-int(a))
if(d==f):
	print("yes")
else:
	print("no")
