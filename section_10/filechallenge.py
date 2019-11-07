# Write a program to append the times tables to our jabberwocky poem
# in sample.txt. We want the tables from 2 to 12 (similar to the output
# from the For loops par 2 lecture in section 6).
#
# The first column of numbers should be right justified. As an example,
# the 2 times table should look like this:
#   1 times 2 is 2
#   2 times 2 is 4
# ...

with open('challenge.txt', 'w') as file:
	for i in range(2, 13):
		for j in range(1, 13):
			print('{:>2} times {} is {}'.format(j, i, i * j), file=file)
		print('-' * 40, file=file)
