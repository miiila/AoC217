
grid = []

with open('Day22_input') as f:
	for l in f.readlines():
		grid.append(list(l.strip()))

directions = {
	'right': {
		'up': (0,1, 'right'),
		'right': (1,0, 'down'),
		'down': (0,-1, 'left'),
		'left': (-1,0, 'up'),
	},
	'left': {
		'up': (0,-1, 'left'),
		'left': (1,0, 'down'),
		'down': (0,1, 'right'),
		'right': (-1,0, 'up'),
	},
	'rev': {
		'up': (1,0, 'down'),
		'left': (0,1, 'right'),
		'down': (-1,0, 'up'),
		'right': (0,-1, 'left'),
	},
	'con': {
		'up': (-1,0, 'up'),
		'left': (0,-1, 'left'),
		'down': (1,0, 'down'),
		'right': (0,1, 'right'),
	},

}

i=0
inf = 0
pos = (len(grid)//2, len(grid[0])//2)
curDir = 'up'
while(i<10000000):
	# for l in grid:
	# 	print(''.join(l))
	# print('\n')

	if (pos[0]) == len(grid):
		grid.append(len(grid[0])*['.'])
	elif (pos[0]) < 0:
		grid.insert(0,len(grid[0])*['.'])
		pos = (0, pos[1])
	if (pos[1]) == len(grid[pos[0]]):
		for l in grid:
			l.append('.')
	elif (pos[1]) < 0:
		for l in grid:
			l.insert(0, '.')
		pos = (pos[0], 0)

	# print(pos, len(grid), len(grid[pos[0]]))
	if grid[pos[0]][pos[1]] == '.':
		grid[pos[0]][pos[1]] = 'W'
		turn = directions['left'][curDir]
	elif grid[pos[0]][pos[1]] == 'W':
		grid[pos[0]][pos[1]] = '#'
		inf += 1
		turn = directions['con'][curDir]
	elif grid[pos[0]][pos[1]] == '#':
		grid[pos[0]][pos[1]] = 'F'
		turn = directions['right'][curDir]
	elif grid[pos[0]][pos[1]] == 'F':
		grid[pos[0]][pos[1]] = '.'
		turn = directions['rev'][curDir]

	curDir = turn[2]	
	pos = (pos[0]+turn[0], pos[1]+turn[1])
	i+=1

print(inf)
# for l in grid:
# 		print(''.join(l))

