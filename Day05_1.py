
with open('Day5_input') as f:
	ins = [int(x.strip()) for x in f.readlines()]

l = len(ins)
i = 0
steps = 0

while(i<l and i>-1):
	next = ins[i]
	if (next >2):
		ins[i]-=1
	else:
		ins[i]+=1
	i += next
	steps+=1

print(steps)