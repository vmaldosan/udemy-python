import sqlite3

db = sqlite3.connect('contacts.sqlite')

updateSql = "UPDATE contacts SET email = 'updated@email.com' WHERE contacts.phone = 1234"
updateCursor = db.cursor()
updateCursor.execute(updateSql)
print('{} rows updated'.format(updateCursor.rowcount))

updateCursor.connection.commit()
updateCursor.close()

for name, phone, email in db.execute('SELECT * FROM contacts'):
  print(name)
  print(phone)
  print(email)
  print('-' * 20)

db.close()
