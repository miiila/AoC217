
res = None
minR = float('inf')

i = 0

accs = []
with open('Day20_input') as f:
	for l in  [l.strip() for l in f]:
		r = 0
		s = 0
		t = 0
		for a in l.split(', ')[2][3:-1].split(','):
			r += abs(int(a))
		for p in l.split(', ')[0][3:-1].split(','):
			s += abs(int(p))
		for v in l.split(', ')[1][3:-1].split(','):
			t += abs(int(v))
		if r <= minR: 
			print(i, s, t,r)
			minR = r
		i+=1

print(accs)