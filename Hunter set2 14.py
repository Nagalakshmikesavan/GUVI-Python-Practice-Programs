n=input()
m=list(n)
from itertools import permutations
p=permutations(m)
for i in p:
	print("".join(i))
