res = 0

with open('Day4_input') as f:
	for l in [x.strip().split(' ') for x in f.readlines()]:
		used = {}
		br = 0
		for w in l:
			if w in used:
				br = 1
				break
			else:
				used[w]=1
		if br == 0:
			res+=1
print(res)