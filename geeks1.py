#Bastin once had trouble finding the numbers in a string. The numbers are distributed in a string across various test cases.
#There are various numbers in each test case you need to find the number in each test case. Each test case has various numbers in sequence. You need to find only those numbers which do not contain 9. For eg, if the string contains "hello this is alpha 5051 and 9475".You will extract 5051 and not 9475. You need only those numbers which are consecutive and you need to help him find the numbers.  
n=input().split()
l=[]
max=0
for i in n:
	if i.isnumeric():
		a=list(i)
		if 9  not in a:
			l.append(i)
		for i in range(len(l)):
			if(int(l[i])>max):
				max=int(l[i])
print(max)
