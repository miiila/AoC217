import sys

limit = 368078

moves =[(0,1), (-1,0), (0,-1), (1,0)]
times = 1
even = 0
move = 0

coord = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
c = (0,0)
grid = {(0,0): 1}
while True:
	if even==2:
		even=0
		times+=1
	for i in range(0, times):
		c = (c[0]+moves[move][0],c[1]+moves[move][1])
		
		grid[c] = 0
		for u in coord:
			if (c[0]+u[0], c[1]+u[1]) in grid:
				grid[c] += grid[(c[0]+u[0], c[1]+u[1])]
		if grid[c] > limit:
			print(grid[c])
			sys.exit()

	even+=1
	move=(move+1)%4