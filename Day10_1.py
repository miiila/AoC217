#1

input = [206,63,255,131,65,80,238,157,254,24,133,2,16,0,1,3]

limit = 256
list = list(range(0,limit))

skip = 0
currentPos = 0

for length in input:
	subList = []
	for i in range(currentPos,currentPos+length):
		i%=limit
		subList.append(list[i])
	subList = subList[::-1]
	for i in range(currentPos,currentPos+length):
		i%=limit
		list[i] = subList.pop(0)
	currentPos = (currentPos+length+skip)%limit
	skip+=1

# print(list)
print(list[0]*list[1])
	
