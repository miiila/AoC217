order = list('abcdefghijklmnop')
dance = order[:]

with open('Day16_input') as f:
	inst = f.readline().strip().split(',')
i = 0
while(str(dance)!=str(order) or i==0):
	for ins in inst:
		move = ins[0]
		target = ins[1:].split('/')

		if move=='s':
			iA = int(target[0])
			dance = dance[-iA:]+dance[0:-iA]
		if move=='p':
			move='x'
			target[0] = dance.index(target[0])
			target[1] = dance.index(target[1])
		if move=='x':
			iA = int(target[0])
			iB = int(target[1])
			tmp = dance[iA]
			dance[iA] = dance[iB]
			dance[iB] = tmp
	i+=1
	print(i,''.join(dance))
