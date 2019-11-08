import pickle

radiohead = (
		'OK Computer',
		'Radiohead',
		'1996',
		(
			(1, 'Airbag'),
			(2, 'No Nurprises'),
			(3, 'Karma Police'),
			(4, 'Paranoid Android')
		)
)

with open('radiohead.pick', 'wb') as pickleFile:
	pickle.dump(radiohead, pickleFile)

with open('radiohead.pick', 'rb') as radioPickled:
	data = pickle.load(radioPickled)

print(data)

album, artist, year, trackList = data

print(album)
print(artist)
print(year)
for track in trackList:
	trackNbr, trackTitle = track
	print('[', end='')
	print(trackNbr, trackTitle, sep=' - ', end='')
	print(']')
