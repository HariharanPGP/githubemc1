First run create_table.py

by
Manjula
.
2:00 pm
Broadcast to all
import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully");

conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print("Table created successfully");
conn.close()