insts = []

with open('Day18_input') as f:
	insts = [l.strip().split() for l in f.readlines()]

lastPlayedFreq = 0
registries = {'a': 0, 'b': 0, 'f': 0, 'i': 0, 'p': 0}

i=0
while (i>=0 or i < len(insts)):
	ins = insts[i]

	if (len(ins) == 3):
		try:
			val = int(ins[2])
		except Exception as e:
			val = registries[ins[2]]

	if ins[0] == 'snd':
		lastPlayedFreq = registries[ins[1]]
	elif ins[0] == 'set':
		registries[ins[1]] = val
	elif ins[0] == 'add':
		registries[ins[1]] += val
	elif ins[0] == 'mul':
		registries[ins[1]] *= val
	elif ins[0] == 'mod':
		registries[ins[1]] %= val
	elif ins[0] == 'rcv':
		if registries[ins[1]] != 0:
			#1
			print(lastPlayedFreq)
			break
	elif ins[0] == 'jgz':
		if registries[ins[1]] > 0:
			i += val
			continue

	i+=1