import math
ops = {}
with open('Day21_input') as f:
	for l in [l.strip().split(' => ') for l in f]:
		ops[l[0]] = l[1]

def flip(pattern):
	return pattern[2]+pattern[1]+pattern[0]+pattern[3]+pattern[6]+pattern[5]+pattern[4]+pattern[7]+pattern[10]+pattern[9]+pattern[8]

def rotate(pattern):
	if len(pattern) == 5:
		yield pattern
		for i in range(0,3):
			pattern = pattern[3]+pattern[0]+pattern[2]+pattern[4]+pattern[1]
			yield pattern
	else:
		for i in range(0,2):
			yield pattern
			for j in range(0,3):
				pattern = pattern[8]+pattern[4]+pattern[0]+pattern[3]+pattern[9]+pattern[5]+pattern[1]+pattern[7]+pattern[10]+pattern[6]+pattern[2]
				yield pattern
			pattern = flip(pattern)

def split(pattern):
	patterns = []
	rows = pattern.split('/')
	if pattern.index('/')%2==0:
		while rows:
			r1 = rows.pop(0)
			r2 = rows.pop(0)
			while r1:
				patterns.append(r1[0:2]+'/'+r2[0:2])
				r1 = r1[2:]
				r2 = r2[2:]
	else:
		while rows:
			r1 = rows.pop(0)
			r2 = rows.pop(0)
			r3 = rows.pop(0)
			while r1:
				patterns.append(r1[0:3]+'/'+r2[0:3]+'/'+r3[0:3])
				r1 = r1[3:]
				r2 = r2[3:]
				r3 = r3[3:]

	return patterns

def enhance(patterns):
	newPatterns = []
	for pattern in patterns:
		for p in rotate(pattern):
			if p in ops:
				newPatterns.append(ops[p])
				break

	return newPatterns

def joinGrid(patterns):
	if (len(patterns) == 1): return patterns[0]
	newGrid = ''
	l = int(math.sqrt(len(patterns)))

	while patterns:
		r=[]
		for i in range(0,l):
			r.append(patterns.pop(0).split('/'))
		while(r[0]):
			for p in r:
				newGrid+=p.pop(0)
			newGrid+='/'
	return newGrid[0:-1]

# Testing outputs
# for p in rotate('#./..'):
# 	for p in p.split('/'):
# 		print(p)
# 	print('\n')

# print('\n')

# for p in rotate('#../..#/...'):
# 	for p in p.split('/'):
# 		print(p)
# 	print('\n')

# print(split('#..#/..../..../#..#'))
# print(split('.#./..#/###'))
# print(split('##.##./#..#../....../##.##./#..#../......'))

# print(enhance(split('.#./..#/###')))
# print(enhance(split('#..#/..../..../#..#')))
# print(joinGrid(enhance(split('#..#/..../..../#..#'))))

# for p in joinGrid(enhance(split('#..#/..../..../#..#'))).split('/'):
# 	print(p)

# with open('somefile.txt', 'a') as the_file:
# 	the_file.write('Hello\n')
# 	while i < 1:
# 		inp = joinGrid(enhance(split(inp)))
# 		the_file.write(inp+'\n')
# 		print(inp.count('#'))
# 		# print(inp)
# 		# for p in inp.split('/'): 
# 		# 	print(p)
# 		# print('\n')
# 		i += 1

# 	print(inp.count('#'))

# inp = '..#...#...#./########.#../##..##.....#/.###.###.##./.#....#.#..#/.#...#..##../.#.....###../.#...##..#../..#...#...#./####.#...#../##.....#...#/.###.##..##.'
inp = '.#./..#/###'
i = 0

while i < 18:
	inp = joinGrid(enhance(split(inp)))
	if i==4:
		print('#1:', inp.count('#'))
	i += 1

print('#2:', inp.count('#'))





