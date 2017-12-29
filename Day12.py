res = 0
used = set()

with open('Day12_input') as f:
	lines = [l.strip().replace(',','').split()[2:] for l in f.readlines()]

def findNextRec(input):
	for i in lines[input]:
		if (int(i) not in used):
			used.add(int(i))
			findNextRec(int(i))

findNextRec(0)
print(len(used))

groups = 1
for i in range(1,len(lines)):
	if (i not in used):
		groups+=1
		findNextRec(i)

print(groups)
