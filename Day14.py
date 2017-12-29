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

#1
res1 = 0
res2 = 0
regions = []

for i in range(0,128):
	region = ''
	for h in knotHash('uugsqrei-'+str(i)):
		res1 += (bin(int(h,16)).count('1'))
		region += str(format(int(h,16), '#06b'))[2:]
	regions.append(list(region))

print(res1)

#2
def markRegionsRec(row, col):
	if regions[row][col] == '1': 
		regions[row][col] = '2'
		if (row-1 >= 0): markRegionsRec(row-1, col)
		if (row+1 < len(regions)): markRegionsRec(row+1, col)
		if (col-1 >= 0): markRegionsRec(row, col-1)
		if (col+1 < len(regions[row])): markRegionsRec(row, col+1)

for i in range(0,len(regions)):
	for j in range(0,len(regions[0])):
		if regions[i][j] == '1':
			res2+=1
			markRegionsRec(i, j)

print(res2)














