
res = {'n': 0, 'ne': 0, 'se': 0, 'sw': 0, 's': 0, 'nw': 0}
opposites = {'n': 's', 's': 'n', 'se': 'nw', 'nw': 'se', 'sw': 'ne', 'ne': 'sw'}

neMax = 0

with open('Day11_input') as f:
	for hex in f.readline().split(','):
		if res[opposites[hex]] > 0: 
			res[opposites[hex]] -= 1
			if (res['n'] + res['ne'] > neMax):
				neMax = res['n'] + res['ne']
		else:
			res[hex] += 1


print(res['n']+max(res['ne'],res['nw']), neMax)
