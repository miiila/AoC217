#2

def knotHash(input):

	input = [ord(a) for a in input]

	input+=[17, 31, 73, 47, 23]

	limit = 256
	listI = list(range(0,limit))

	skip = 0
	currentPos = 0

	for round in range(0,64):
		for length in input:
			subList = []
			for i in range(currentPos,currentPos+length):
				i%=limit
				subList.append(listI[i])
			subList = subList[::-1]
			for i in range(currentPos,currentPos+length):
				i%=limit
				listI[i] = subList.pop(0)
			currentPos = (currentPos+length+skip)%limit
			skip+=1

	xor = []
	i = 0
	res = 0

	for j in listI:
		res^=j
		if i==15:
			xor.append(res)
			res=0
			i=0
		else:
			i+=1

	return ''.join([format(s, '02x') for s in xor])

print(knotHash('206,63,255,131,65,80,238,157,254,24,133,2,16,0,1,3'))
	
