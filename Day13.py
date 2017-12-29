
firewall = {}

with open('Day13_input') as f:
	for l in f.readlines():
		l = l.replace(':','').split()
		firewall[int(l[0])] = int(l[1])

#1

score = 0

for i in range(0,max(firewall)+1):
	if i in firewall and i%((firewall[i]*2)-2)==0:
		score += i*firewall[i]

print(score)

#2

delay = 0
caught = True
while(caught):
	caught = False
	delay+=1
	for i in range(0,max(firewall)+1):
		if i in firewall and (i+delay)%((firewall[i]*2)-2)==0:
			caught = True
			break

print(delay)
