n=input()
b=list(n)
a=' '
for i in b:
	if i==' ':
		i.replace(" ","")
	
	else:
		a=a+i
print(a.strip())
