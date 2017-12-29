
state = []
with open('Day20_input') as f:
	for l in  [l.strip() for l in f]:
		part = {}
		part['p'] = tuple([int(p) for p in l.split(', ')[0][3:-1].split(',')])
		part['v'] = tuple([int(v) for v in l.split(', ')[1][3:-1].split(',')])
		part['a'] = tuple([int(a) for a in l.split(', ')[2][3:-1].split(',')])
		state.append(part)

while True:
	collisions = {}
	toRemove = set()
	res = 0

	for i,part in enumerate(state):
		if part == None: continue
		res += 1
		part['v'] = (part['v'][0] + part['a'][0], part['v'][1] + part['a'][1], part['v'][2] + part['a'][2])
		part['p'] = (part['p'][0] + part['v'][0], part['p'][1] + part['v'][1], part['p'][2] + part['v'][2])
		if part['p'] in collisions:
			toRemove.add(i)
			toRemove.add(collisions[part['p']])
		else:
			collisions[part['p']] = i

	for i in toRemove:
		state[i] = None

	print(res)