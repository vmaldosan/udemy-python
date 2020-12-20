import sqlite3

db = sqlite3.connect('contacts.sqlite')

newEmail = 'updated@email.com'
phone = input('Please enter the phone number: ')

# updateSql = "UPDATE contacts SET email = 'updated@email.com' WHERE contacts.phone = 1234"
updateSql = 'UPDATE contacts SET email = ? WHERE contacts.phone = ?'
updateCursor = db.cursor()
updateCursor.execute(updateSql, (newEmail, phone))
print('{} rows updated'.format(updateCursor.rowcount))

updateCursor.connection.commit()
updateCursor.close()

for name, phone, email in db.execute('SELECT * FROM contacts'):
  print(name)
  print(phone)
  print(email)
  print('-' * 20)

db.close()
