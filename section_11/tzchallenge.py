import datetime
import pytz

timeZones = [
	'Europe/Madrid',
	'Europe/Dublin',
	'Asia/Tokyo',
	'America/Caracas',
	'Pacific/Auckland',
	'Asia/Kolkata',
	'Europe/Warsaw',
	'Pacific/Honolulu',
	'Asia/Ho_Chi_Minh']

print('Select a time zone, or 0 to quit:')
i = 1
for tz in timeZones:
	print('{} - {}'.format(i, tz))
	i += 1

while True:
	choice = int(input())

	if choice == 0:
		break

	tzName = timeZones[choice - 1]
	tzChoice = pytz.timezone(tzName)
	chosenTime = datetime.datetime.now(tz=tzChoice)
	print('The time in {} is {}'.format(tzName, chosenTime.strftime('%A %x %X %z'), chosenTime.tzname()))
	utcTime = datetime.datetime.utcnow()
	print('Local time is {}'.format(datetime.datetime.now().strftime('%A %x %X')))
	print('UTC time is {}'.format(datetime.datetime.utcnow().strftime('%A %x %X')))
	print()
