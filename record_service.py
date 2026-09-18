
from database import get_connection
from file_handler import load_records, save_records

def add_record():
    print("\n--- Add Student ---")

    try:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        email = input("Enter email: ")

        if not name or not course or not email:
            print("All fields are required.")
            return

        connection = get_connection()

        if connection is None:
            return

        cursor = connection.cursor()

        query = """
        INSERT INTO students (id, name, age, course, email)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (student_id, name, age, course, email)

        cursor.execute(query, values)
        connection.commit()

        print("Record added successfully!")
        print("Student ID:", student_id)

        # Save copy in JSON file
        records = load_records()

        records.append({
            "id": student_id,
            "name": name,
            "age": age,
            "course": course,
            "email": email
        })

        save_records(records)

        cursor.close()
        connection.close()

    except ValueError:
        print("Student ID and Age must be numbers.")

    except Exception as e:
        print("Error:", e)






def view_records():
    print("\n--- Student Records ---")

    try:
        connection = get_connection()

        if connection is None:
            return

        cursor = connection.cursor()

        query = """
        SELECT id, name, age, course, email
        FROM students
        ORDER BY id
        """

        cursor.execute(query)

        records = cursor.fetchall()

        if not records:
            print("No records found.")

        else:
            for record in records:
                print("--------------------------------")
                print("ID:", record[0])
                print("Name:", record[1])
                print("Age:", record[2])
                print("Course:", record[3])
                print("Email:", record[4])

        cursor.close()
        connection.close()

    except Exception as e:
        print("Error:", e)


def search_record():
    print("\n--- Search Student ---")

    try:
        student_id = int(input("Enter student ID: "))

        connection = get_connection()

        if connection is None:
            return

        cursor = connection.cursor()

        query = """
        SELECT id, name, age, course, email
        FROM students
        WHERE id = %s
        """

        cursor.execute(query, (student_id,))

        record = cursor.fetchone()

        if record:
            print("\nRecord Found")
            print("--------------------------------")
            print("ID:", record[0])
            print("Name:", record[1])
            print("Age:", record[2])
            print("Course:", record[3])
            print("Email:", record[4])

        else:
            print("Record not found.")

        cursor.close()
        connection.close()

    except ValueError:
        print("Please enter a valid numeric ID.")

    except Exception as e:
        print("Error:", e)


def update_record():
    print("\n--- Update Student ---")

    try:
        student_id = int(input("Enter student ID: "))

        name = input("Enter new name: ").strip()
        age = int(input("Enter new age: "))
        course = input("Enter new course: ").strip()
        email = input("Enter new email: ").strip()

        if not name or not course or not email:
            print("All fields are required.")
            return

        connection = get_connection()

        if connection is None:
            return

        cursor = connection.cursor()

        query = """
        UPDATE students
        SET name = %s,
            age = %s,
            course = %s,
            email = %s
        WHERE id = %s
        """

        values = (name, age, course, email, student_id)

        cursor.execute(query, values)
        connection.commit()

        if cursor.rowcount > 0:
            print("Record updated successfully!")

            # Update JSON file
            records = load_records()

            for record in records:
                if record["id"] == student_id:
                    record["name"] = name
                    record["age"] = age
                    record["course"] = course
                    record["email"] = email

            save_records(records)

        else:
            print("Record not found.")

        cursor.close()
        connection.close()

    except ValueError:
        print("Age and ID must be numbers.")

    except Exception as e:
        print("Error:", e)


def delete_record():
    print("\n--- Delete Student ---")

    try:
        student_id = int(input("Enter student ID: "))

        connection = get_connection()

        if connection is None:
            return

        cursor = connection.cursor()

        query = "DELETE FROM students WHERE id = %s"

        cursor.execute(query, (student_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print("Record deleted successfully!")

            # Remove record from JSON file
            records = load_records()

            records = [
                record for record in records
                if record["id"] != student_id
            ]

            save_records(records)

        else:
            print("Record not found.")

        cursor.close()
        connection.close()

    except ValueError:
        print("Please enter a valid ID.")

    except Exception as e:
        print("Error:", e)
