def center_print(*args, sep=' ', end='\n', file=None, flush=False):
	text = ''
	i = 0
	for arg in args:
		text += str(arg)
		if i < len(args) - 1:
			text += sep
		i += 1
	left_margin = (80 - len(text)) // 2
	print(' ' * left_margin, text, end=end, file=file, flush=flush)


center_print('Testing 1')
center_print('Testing', '2')
center_print('Test', 'ing', '3', sep='-')
center_print('Testing', '4', end='.\n')
with open('centred', mode='w') as centredFile:
	center_print('Testing 5', file=centredFile)
