
with open('Day9_input') as f:

	res = 0
	score = 0
	skip = False
	skipOnce = False
	garb = 0

	for c in f.readline():
		if skipOnce:
			skipOnce = False
			continue
		if c=='!':
			skipOnce = True
			continue
		if c=='>':
			skip=False
		if skip:
			garb+=1
			continue
		if c=='{':
			score+=1
		if c=='}':
			res+=score
			score-=1
		if c=='<':
			skip = True

print(res, garb)