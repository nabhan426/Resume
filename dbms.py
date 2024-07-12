import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create and return a database connection."""
    return mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="nabhan2004",
        database="nabhan_class"
    )

def create_students_table():
    """Create the students table in the database."""
    try:
        conn = create_connection()
        cursor = conn.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS students (
            id INT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            major VARCHAR(100)
        );
        """
        cursor.execute(create_table_query)
        conn.commit()
        print("Students table created successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def create_student(student_id, name, age, major):
    """Create a new student in the database."""
    try:
        conn = create_connection()
        cursor = conn.cursor()
        insert_query = "INSERT INTO students (id, name, age, major) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (student_id, name, age, major))
        conn.commit()
        print("Student created successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def read_students():
    """Read and print all students from the database."""
    try:
        conn = create_connection()
        cursor = conn.cursor()
        select_query = "SELECT * FROM students"
        cursor.execute(select_query)
        records = cursor.fetchall()

        print("Number of students in the database:", cursor.rowcount)
        print("Student details:")
        for row in records:
            print("Student Id:", row[0])
            print("Student Name:", row[1])
            print("Student Age:", row[2])
            print("Student Major:", row[3])
            print()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def update_student(student_id, name=None, age=None, major=None):
    """Update an existing student in the database."""
    try:
        conn = create_connection()
        cursor = conn.cursor()
        update_fields = []
        params = []
        
        if name:
            update_fields.append("name = %s")
            params.append(name)
        if age:
            update_fields.append("age = %s")
            params.append(age)
        if major:
            update_fields.append("major = %s")
            params.append(major)
        
        params.append(student_id)
        update_query = f"UPDATE students SET {', '.join(update_fields)} WHERE id = %s"
        cursor.execute(update_query, params)
        conn.commit()
        print("Student updated successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def delete_student(student_id):
    """Delete a student from the database."""
    try:
        conn = create_connection()
        cursor = conn.cursor()
        delete_query = "DELETE FROM students WHERE id = %s"
        cursor.execute(delete_query, (student_id,))
        conn.commit()
        print("Student deleted successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Example Usage:
create_students_table()

create_student(1, "arun", 20, "Computer Science")
create_student(2, "kumar", 22, "Mathematics")

read_students()

update_student(1, name="sidharth", age=21)

read_students()

delete_student(2)

read_students()
