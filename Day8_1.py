
registers = {}
res2 = 0

with open('Day8_input') as f:
	for l in f.readlines():
		l = [l.strip() for l in l.split()]
		if l[0] not in registers:
			registers[l[0]] = 0
		if l[4] not in registers:
			registers[l[4]] = 0
		if eval("{:d} {:s} {:d}".format(registers[l[4]], l[5], int(l[6]))):
			if l[1]=='inc':
				registers[l[0]]+=int(l[2]) 
			else:
				registers[l[0]]-=int(l[2])
			if registers[l[0]] > res2:
				res2 = registers[l[0]] 

res1 = 0
for k in registers:
	if registers[k] > res1:
		res1 = registers[k]

print(res1,res2)


