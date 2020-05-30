# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on a 18-30 holiday (they must be
# over 19 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.

name = input('Write your name: ')
age = int(input('Write your age: '))
if 18 <= age <= 30:
	print('Welcome, {}!'.format(name))
else:
	print('Go home, {}!'.format(name))
