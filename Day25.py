
state = 'A'
steps = 12134527
# ones = 0
i = 0
head = 0
tape = [0]

ops = {
	'A': {
		0: (1, 1, 'B'),
		1: (0, -1, 'C')
	},
	'B': {
		0: (1, -1, 'A'),
		1: (1, 1, 'C')
	},
	'C': {
		0: (1, 1, 'A'),
		1: (0, -1, 'D')
	},
	'D': {
		0: (1, -1, 'E'),
		1: (1, -1, 'C')
	},
	'E': {
		0: (1, 1, 'F'),
		1: (1, 1, 'A')
	},
	'F': {
		0: (1, 1, 'A'),
		1: (1, 1, 'E')
	},
}


while i < steps:
	# if (i%100000==0): print(i)
	if head == -1:
		tape.insert(0, 0)
		head = 0
	elif head == len(tape):
		tape.append(0)

	op = ops[state][tape[head]]
	tape[head] = op[0]
	head += op[1]
	state = op[2]
	i+=1

print(tape.count(1))