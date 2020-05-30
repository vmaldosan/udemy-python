ipadd = "127.12." # input('Enter IP: ')
if ipadd[-1] != '.':
	ipadd += '.'
numSeg = 1
lenSeg = 0
for i in ipadd:
	if i == '.':
		print('Length of segment {}: {}'.format(numSeg, lenSeg))
		numSeg += 1
		lenSeg = 0

	else:
		lenSeg += 1
