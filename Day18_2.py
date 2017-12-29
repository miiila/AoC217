insts = []

with open('Day18_input') as f:
	insts = [l.strip().split() for l in f.readlines()]

regs = ({'a': 0, 'b': 0, 'f': 0, 'i': 0, 'p': 0}, {'a': 0, 'b': 0, 'f': 0, 'i': 0, 'p': 1})
qus = ([], [])
nexts = [0,0]
finished = [False, False]
sent = [0, 0]
current = 0

while (not finished[0] or not finished[1]):
	if (nexts[current] < 0 or nexts[current] > len(insts)):
		finished[current] = True

	ins = insts[nexts[current]]

	if (len(ins) == 3):
		try:
			val = int(ins[2])
		except Exception as e:
			val = regs[current][ins[2]]

	if ins[0] == 'snd':
		sent[current] += 1
		qus[current^1].append(regs[current][ins[1]])
		finished[current^1] = False
	elif ins[0] == 'set':
		regs[current][ins[1]] = val
	elif ins[0] == 'add':
		regs[current][ins[1]] += val
	elif ins[0] == 'mul':
		regs[current][ins[1]] *= val
	elif ins[0] == 'mod':
		regs[current][ins[1]] %= val
	elif ins[0] == 'rcv':
		if len(qus[current]) == 0:
			finished[current] = True
			current ^= 1
			continue
		else:
			finished[current] = False
			regs[current][ins[1]] = qus[current].pop(0)
	elif ins[0] == 'jgz':
		if ins[1] == '1':
			nexts[current] += val
			continue
		elif regs[current][ins[1]] > 0:
			nexts[current] += val
			continue

	nexts[current]+=1

print(sent[1])