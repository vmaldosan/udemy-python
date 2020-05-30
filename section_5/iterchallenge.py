oddList = list(range(1, 10, 2)) #[1, 3, 5, 7]
liter = iter(oddList)

for i in range(len(oddList)):
	print(next(liter))
