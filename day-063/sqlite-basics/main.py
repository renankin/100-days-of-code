import sqlite3

db = sqlite3.connect("books-collection.db")

cursor = db.cursor()

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', "
               "'9.3')")
db.commit()
