res = 0

with open('Day4_input') as f:
	for l in [x.strip().split(' ') for x in f.readlines()]:
		used = {}
		br = 0
		for w in l:
			alph = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
			for k in w:
				alph[ord(k)-ord('a')]+=1
			if str(alph) in used:
				br = 1
				break
			else:
				used[str(alph)]=1
		if br == 0:
			res+=1
print(res)