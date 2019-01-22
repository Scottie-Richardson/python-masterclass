import sqlite3

conn = sqlite3.connect("contacts.sqlite")

name = input("Please enter a name to search for: ")

# The sqlite placeholder is ?, this will possible be different depending on database platform
# Also, the variable has to be passed to the SQL statment as a tuple
for row in conn.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):
    print(row)

conn.close()
