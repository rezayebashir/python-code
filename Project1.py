import sqlite3

# 1. Create/connect to university.db
conn = sqlite3.connect("university.db")
cursor = conn.cursor()

# Drop table if it already exists (so you can run the script cleanly multiple times)
cursor.execute("DROP TABLE IF EXISTS students")

# 2. Create a 'students' table
cursor.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    semester INTEGER NOT NULL,
    gpa REAL
)
""")

# 3. Insert at least five students using parameterized queries (?)
students_data = [
    ("Ahmad", "Computer Science", 1, 3.95),
    ("Zahra", "Software Engineering", 2, 3.88),
    ("Omid", "Computer Science", 1, 3.70),
    ("Maryam", "Data Science", 3, 3.92),
    ("Bilal", "Information Technology", 2, 3.60)
]

cursor.executemany(
    "INSERT INTO students (name, department, semester, gpa) VALUES (?, ?, ?, ?)",
    students_data
)
conn.commit()

# 4. Display all records
print("--- 1. All Students ---")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# 5. Search by semester (e.g., Semester 1)
target_semester = 1
print(f"\n--- 2. Students in Semester {target_semester} ---")
cursor.execute("SELECT * FROM students WHERE semester = ?", (target_semester,))
for row in cursor.fetchall():
    print(row)

# 6. Update one student's department (e.g., change student with ID 3 to Artificial Intelligence)
cursor.execute(
    "UPDATE students SET department = ? WHERE id = ?",
    ("Artificial Intelligence", 3)
)
conn.commit()
print("\n--- 3. Updated Student ID 3's Department ---")

# 7. Delete one record by ID (e.g., delete student with ID 5)
cursor.execute("DELETE FROM students WHERE id = ?", (5,))
conn.commit()
print("--- 4. Deleted Student with ID 5 ---")

# 8. Print the final table contents
print("\n--- 5. Final Table Contents ---")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# Close the database connection
conn.close()
