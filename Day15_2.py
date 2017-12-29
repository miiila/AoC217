
inputA = 277
inputB = 349

score = 0

queueA = []
queueB = []

i = 0
while len(queueA) < (5*(10**6)):
	inputA = (inputA*16807)%2147483647
	if inputA%4 == 0: queueA.append(inputA)
	
while len(queueB) < (5*(10**6)):
	inputB = (inputB*48271)%2147483647
	if inputB%8 == 0: queueB.append(inputB)


for i in range(0,(5*(10**6))):
	if (queueA[i] & 0b1111111111111111) == (queueB[i] & 0b1111111111111111): score+=1

print(score)