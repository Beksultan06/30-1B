import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER   
    )
""")

cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Bob", 21))

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("UPDATE students SET age = ? WHERE name = ?", (22, 'Bob'))

cursor.execute("DELETE FROM students WHERE name = ?", ("Bob",))

conn.commit()
conn.close()