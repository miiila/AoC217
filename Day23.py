def isPrime(n):
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return False

	return True

regs = 'abcdefgh'
registers = {}

for c in regs:
	registers[c] = 0
registers['a'] = 1

with open('Day23_input') as f:
	prg = [l.strip().split() for l in f]

cur = 0
mul = 0
i = 0
while (cur > -1 and cur < len(prg)):
	i+=1
	ins = prg[cur][0]
		
	if(prg[cur][1]=='h' and isPrime(registers['b'])): 
		cur += 1
		continue

	try:
		valA = int(prg[cur][1])
	except Exception as e:
		valA = registers[prg[cur][1]]
	try:
		valB = int(prg[cur][2])
	except Exception as e:
		valB = registers[prg[cur][2]]

	if ins == 'set':
		registers[prg[cur][1]] = valB
		cur += 1
	elif ins == 'sub':
		registers[prg[cur][1]] -= valB
		cur += 1
	elif ins == 'mul':
		registers[prg[cur][1]] *= valB
		mul += 1
		cur += 1
	elif ins == 'jnz':
		if valA != 0:
			cur += valB
		else:
			cur += 1

print(registers['h'])


