
inputA = 277
inputB = 349
score = 0

for i in range(0,((40*(10**6))+1)):
	inputA = (inputA*16807)%2147483647
	inputB = (inputB*48271)%2147483647
	if (inputA & 65535) == (inputB & 65535): score+=1

print(score)