from math import ceil
t = 368078

# first diagonal
k = 1
i = 0

while k<t:
	i+=1
	k+=i*2
	

step1 = ceil((i-1)/2)
diag1 = k-(i*2)

# second diagonal
k = 1
i = 0
l = 1

while k<t:
	if l==1:
		i+=1
		l=0
	else:
		l=1
	k+=i*4

step2 = ceil(i)
diag2 = k	

print(abs((diag2+diag1)//2 - t) + step2)