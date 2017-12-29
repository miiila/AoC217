res = 0

with open('Day2_input') as f:
	for line in f.readlines():
		line = [int(x.strip()) for x in line.split(',')]
		line.sort()
		line.reverse()
		
		for i,v in enumerate(line):
			for j in range(i+1, len(line)):
				x = v/line[j]
				if (x%1 == 0): 
					res += x
					break
print(res)
