
lines = []

with open('Day19_input') as f:

	for line in [l.replace('\n', '') for l in f.readlines()]:

		lines.append(line)

go = True

direction = {'row': 0, 'col': 75}
d = 1
last = '|'
k = 'row'
res = ''
steps = 0
while(go):
	steps+=1
	pos = lines[direction['row']][direction['col']]
	if pos == '+':
		if last == '|':
			k = 'col'
			if direction['col'] == 0 or lines[direction['row']][direction['col']-1] == ' ':
				d = 1
			else:
				d = -1
		else:
			k = 'row'
			if direction['row'] == 0 or lines[direction['row']-1][direction['col']] == ' ':
					d = 1
			else:
				d = -1
	elif pos != '|' and pos!='-':
		res+=pos

	if pos == 'Q': go = False
	last = pos
	direction[k]+=d

print(res,steps)