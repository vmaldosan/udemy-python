import sqlite3

db = sqlite3.connect('contacts.sqlite')
db.execute('CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)')
db.execute("INSERT INTO contacts VALUES ('Victor', 23452345, 'victor@email.com')")
db.execute("INSERT INTO contacts VALUES ('Brian', 1234, 'brian@myemail.com')")

cursor = db.cursor()
cursor.execute('SELECT * FROM contacts')

# print(cursor.fetchall())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

for row in cursor:
  print(row)

cursor.close()
db.commit()
db.close()
