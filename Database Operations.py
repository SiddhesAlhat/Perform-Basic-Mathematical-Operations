import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(
            database="student_db",
            user="postgres",
            password="your_password",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print("Database connection failed:", e)

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            email VARCHAR(100)
        )
    """)
    conn.commit()
    cursor.close()

def insert_student(conn):
    try:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        email = input("Enter email: ")

        cursor = conn.cursor()
        query = "INSERT INTO students (name, age, email) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, age, email))
        conn.commit()
        cursor.close()
        print("✅ Student inserted successfully")
    except Exception as e:
        print("❌ Error inserting data:", e)

def view_students(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    print("\nID | Name | Age | Email")
    print("-" * 30)
    for row in records:
        print(row)

    cursor.close()

def update_student(conn):
    try:
        sid = int(input("Enter student ID to update: "))
        age = int(input("Enter new age: "))

        cursor = conn.cursor()
        query = "UPDATE students SET age=%s WHERE id=%s"
        cursor.execute(query, (age, sid))
        conn.commit()
        cursor.close()
        print("✅ Student updated successfully")
    except Exception as e:
        print("❌ Error updating record:", e)

def delete_student(conn):
    try:
        sid = int(input("Enter student ID to delete: "))

        cursor = conn.cursor()
        query = "DELETE FROM students WHERE id=%s"
        cursor.execute(query, (sid,))
        conn.commit()
        cursor.close()
        print("✅ Student deleted successfully")
    except Exception as e:
        print("❌ Error deleting record:", e)

def main():
    conn = connect_db()
    if conn is None:
        return

    create_table(conn)

    while True:
        print("\n===== Student Database Menu =====")
        print("1. Insert Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            insert_student(conn)
        elif choice == '2':
            view_students(conn)
        elif choice == '3':
            update_student(conn)
        elif choice == '4':
            delete_student(conn)
        elif choice == '5':
            print("Exiting application...")
            break
        else:
            print("❌ Invalid choice")

    conn.close()

if __name__ == "__main__":
    main()
