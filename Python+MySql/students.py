

# 🎓 Student Management System (Python + MySQL)

import mysql.connector
def admin_login(cursor):
     username=input("enter your username")
     password=input("enter your password")
     query="select * from admin where username=%s and password=%s"
     cursor.execute(query,(username,password))
     record=cursor.fetchone()
     if record:
          print("admin login succesfull")
          return True
     else:
          print("invalid admin credentails")
          return False
def add(cursor,connection):
        print("\n--- Admin Verification Required ---")
        if not admin_login(cursor):
            print("Access denied. Returning to main menu.")
            return
        name=input("enter student name").strip()
        rollno=input("enter student roll no").strip()
        marks=input("enter student marks").strip()
        query="insert into students (name,rollno,marks) values(%s,%s,%s)"
        cursor.execute(query,(name,rollno,marks))
        connection.commit()
        print("student rercords added succesfully")

def view(cursor):
    query="select * from students"
    cursor.execute(query)
    records=cursor.fetchall()
    if records:
        print("All Students Records")
        for row in records:
            print(f"name-{row[0]}, rollno-{row[1]}, marks-{row[2]}")
    else:
        print("student records not found")
    

def search(cursor):
    rollnotosearch=input("search by roll no").strip()
    query="select *from students where rollno=%s"
    cursor.execute(query,(rollnotosearch,))
    record=cursor.fetchone()
    if record:
        print("Student Record  Found")
        print(f"name-{record[0]}, rollno-{record[1]}, marks-{record[2]}")
    else:
        print("Student Record Not Found")

def delete(cursor,connection):
        print("\n--- Admin Verification Required ---")
        if not admin_login(cursor):
            print("Access denied. Returning to main menu.")
            return
        rolltodelete=input("delete by roll no").strip()
        query="delete from students where rollno=%s"
        cursor.execute(query,(rolltodelete,))
        connection.commit()
        if cursor.rowcount > 0:
            print(f" Record with roll no {rolltodelete} deleted successfully.")
        else:
            print(f" No record found with roll no {rolltodelete}.")

def update(cursor,connection):
        print("\n--- Admin Verification Required ---")
        if not admin_login(cursor):
            print("Access denied. Returning to main menu.")
            return
        rolltoup=input("update  by roll no").strip()
        newname=input("enter newname")
        newmarks=input("enter newmarks")
        query="update students set name=%s,marks=%s where rollno=%s"
        cursor.execute(query,(newname,newmarks,rolltoup))
        connection.commit()
        if cursor.rowcount > 0:
            print(" Record updated successfully.")
        else:
            print(" No record found with that roll number.")
def add_skills(cursor, connection):
    roll = input("Enter roll number: ").strip()

    # Check if roll exists
    cursor.execute("SELECT * FROM students WHERE rollno=%s", (roll,))
    record = cursor.fetchone()

    if not record:
        print(" Student not found with this roll number")
        return

    skills = input("Enter skills (comma separated): ").strip()
    query = "UPDATE students SET skills=%s WHERE rollno=%s"
    cursor.execute(query, (skills, roll))
    connection.commit()
    print(" Skills added successfully!")

def update_skills(cursor, connection):
    roll = input("Enter roll number: ").strip()

    cursor.execute("SELECT * FROM students WHERE rollno=%s", (roll,))
    record = cursor.fetchone()

    if not record:
        print(" Student not found with this roll number")
        return

    new_skills = input("Enter new skills (comma separated): ").strip()
    query = "UPDATE students SET skills=%s WHERE rollno=%s"
    cursor.execute(query, (new_skills, roll))
    connection.commit()

    print(" Skills replaced successfully!")


def search_by_skill(cursor):
    skill = input("Enter skill to search students: ").strip()
    query = "SELECT name, rollno, skills FROM students WHERE skills LIKE %s"
    cursor.execute(query, ("%"+skill+"%",))
    result = cursor.fetchall()
    if result:
        for row in result:
            print(f"name-{row[0]}, rollno-{row[1]}, skills-{row[2]}")
    else:
        print("No students found with this skill")

def add_business_idea(cursor, connection):
    roll = input("Enter roll number: ").strip()

    # Check if roll exists
    cursor.execute("SELECT * FROM students WHERE rollno=%s", (roll,))
    record = cursor.fetchone()

    if not record:
        print(" Student not found with this roll number")
        return

    idea = input("Enter your business idea: ").strip()
    query = "UPDATE students SET business_idea=%s WHERE rollno=%s"
    cursor.execute(query, (idea, roll))
    connection.commit()
    print(" Business idea submitted!")


try:
    connection=mysql.connector.connect(
        host="****",
        user="****",
        password="*****",
        database="students_db"
    )
   
    if connection.is_connected():
         print("MySql connected succesfully")

         cursor=connection.cursor()

    while True:
        print("\n -----👨‍🎓 Student Management System -----")
        print(" 1.Add Student \n 2.View Student \n 3.Search student \n 4.delete Student \n 5.update student \n 6.Add Skills \n 7.Search By Skill \n 8.Add Business Idea \n 9.Update Skills \n 10.Exit")
        ch=input("enter the option").strip()
        if ch=='1': add(cursor,connection)
        elif ch=='2':view(cursor)
        elif ch=='3':search(cursor)
        elif ch=='4':delete(cursor,connection)
        elif ch=='5':update(cursor,connection)
        elif ch=='6':add_skills(cursor,connection)
        elif ch=='7': search_by_skill(cursor)
        elif ch=='8': add_business_idea(cursor,connection)
        elif ch=='9': update_skills(cursor, connection)
        elif ch=='10':
            print("Exited succesfully")  
            break
        else:print("invalid choice")
except Exception as e:
    print(e)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySql connection closed")
