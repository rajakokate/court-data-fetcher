import sqlite3
with sqlite3.connect('cases.db') as conn,\
 open('schema.sql') as f:
    conn.executescript(f.read())
print("Database initialized.") 