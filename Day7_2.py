import sys

weights = {}

def wRec(name):
	if (weights[name]['sumW'] == 0):
		ch = set()
		weights[name]['sumW'] = weights[name]['w'] 
		for n in weights[name]['child']:
			nw = wRec(n)
			ch.add(nw)
			weights[name]['sumW'] += nw

		if (len(ch)>1):
			for c in weights[name]['child']:
				print(c, weights[c]['w'], weights[c]['sumW'])
			sys.exit()

	return weights[name]['sumW']


with open('Day7_input') as f:
	l = [x.strip() for x in f.readlines()]
	for x in l:
		a = x.split()
		weights[a[0]] = {'w': int(a[1][1:a[1].index(')')]), 'child': [], 'sumW': 0}
		if (len(a) > 2):
			weights[a[0]]['child'] = [s.strip(',') for s in a[3:]]

for d in weights:
	wRec(d)
