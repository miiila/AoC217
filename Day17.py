step = 376

#1
current = 0
res = [0]

for i in range(1,2018):
	current = ((current+step)%len(res))+1
	res.insert((current), i)

print(res[current+1])

#2
current = 0
lenRes = 1
res = []
for i in range(1,50000001):
	current = ((current+step)%lenRes)+1
	lenRes+=1
	if(current == 1): 
		print('.')
		res.insert(0, i)

print(res[0])

