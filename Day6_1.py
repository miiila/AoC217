import operator
mem = [0,5,10,0,11,14,13,4,11,8,8,7,1,4,12,11]

states = []

while mem.__str__() not in states:
	states.append(mem.__str__())
	index, value = max(enumerate(mem), key=operator.itemgetter(1))
	mem[index] = 0
	while value>0:
		index = (index+1)%len(mem)
		mem[index]+=1
		value-=1

print(len(states))
print(len(states)-states.index(mem.__str__()))


