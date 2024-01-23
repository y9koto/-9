import sqlite3

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()

#CREATE TABLE
#cur.execute("CREATE TABLE Users (name TEXT);")

#INSERT
names = input("Add name: ")
cur.execute(f"INSERT INTO Users (name) VALUES ('{names}');")

connection.commit()

connection.close()