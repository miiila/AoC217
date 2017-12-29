comps = []

with open('Day24_input') as f:
	comps = [(int(m[0]), int(m[1])) for m in [l.strip().split('/') for l in f]]

maxSt = []
maxLen = []
lenSt = {}
def makeBridgeRec(bridge, comps, curPins, st):
	maxSt.append(st)
	maxLen.append(len(bridge))
	if (len(bridge) not in lenSt or st > lenSt[len(bridge)]):		
		lenSt[len(bridge)] = st
	for i,c in enumerate(comps):
		if c[0] == curPins or c[1] == curPins:
			newBridge = bridge[:]
			if c[0] == curPins:
				newPins = c[1]
			else:
				newPins = c[0]
			newBridge.append(c)
			makeBridgeRec(newBridge, comps[0:i]+comps[i+1:], newPins, st+c[0]+c[1])


makeBridgeRec([], comps, 0, 0)

print(max(maxSt))
print(lenSt[max(maxLen)])

