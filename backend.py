import pymysql
import time

class SchoolManagement:
    def __init__(self):
        self.con = pymysql.connect(host="localhost", user="root", password="maoji@123", database='sm')
        self.cu = self.con.cursor()

    def check_ele(self, table, admin_no):
        self.cu.execute(f"SELECT * FROM {table} WHERE Admin_no={admin_no}")
        b = self.cu.fetchall()
        c = self.cu.rowcount
        return c

    def add_student(self, admin_no, name, gender, class_, father_name, mother_name, contact_no, dob):
        # Validate inputs
        if not (admin_no.isdigit() and len(admin_no) >= 3):
            return "Admin_no should be numeric and minimum 3 digits"

        if self.check_ele("student", admin_no) >= 1:
            return f"Admin_no {admin_no} already exists!"

        if len(name) > 60:
            return "Name should not exceed 60 characters"

        if not (class_.isdigit() and len(class_) <= 2 and 6 <= int(class_) <= 12):
            return "Class should be between 6 to 12"

        if gender not in ['M', 'F']:
            return "Gender should be M or F"

        if len(father_name) > 60:
            return "Father name should not exceed 60 characters"

        if len(mother_name) > 60:
            return "Mother name should not exceed 60 characters"

        if not (contact_no.isdigit() and len(contact_no) == 10):
            return "Contact no must be numeric and 10 digits"

        # Insert into database
        query = ("INSERT INTO student (Admin_no, Name, Gender, Class, Father_name, Mother_name, Contact_no, DOB) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        data = (admin_no, name.title(), gender.upper(), class_, father_name.title(), mother_name.title(), contact_no, dob)
        self.cu.execute(query, data)
        self.con.commit()
        return "Student added successfully!"

    def search_student(self, admin_no):
        if not self.check_ele("student", admin_no):
            return None

        self.cu.execute(f"SELECT * FROM student WHERE Admin_no={admin_no}")
        return self.cu.fetchone()

    def update_student(self, admin_no, field, value):
        fields = {
            'name': 'Name',
            'gender': 'Gender',
            'class': 'Class',
            'father_name': 'Father_name',
            'mother_name': 'Mother_name',
            'contact_no': 'Contact_no',
            'dob': 'DOB'
        }

        if field not in fields:
            return "Invalid field"

        # Basic validation
        if field == 'name' and len(value) > 60:
            return "Name too long"
        elif field == 'gender' and value.upper() not in ['M', 'F']:
            return "Invalid gender"
        elif field == 'class' and not (value.isdigit() and 6 <= int(value) <= 12):
            return "Invalid class"
        elif field == 'contact_no' and not (value.isdigit() and len(value) == 10):
            return "Invalid contact"

        self.cu.execute(f"UPDATE student SET {fields[field]}='{value}' WHERE Admin_no={admin_no}")
        self.con.commit()
        return "Updated successfully"

    def add_exam_marks(self, admin_no, physics, chemistry, biology, maths, cs, hindi, english):
        if not self.check_ele("student", admin_no):
            return "Student does not exist"

        if self.check_ele("exam", admin_no) > 0:
            return "Marks already exist for this student"

        # Validate marks
        marks = [physics, chemistry, biology, maths, cs, hindi, english]
        subjects = ['Physics', 'Chemistry', 'Biology', 'Maths', 'CS', 'Hindi', 'English']
        max_marks = [70, 70, 70, 80, 70, 80, 80]

        for i, mark in enumerate(marks):
            if not (isinstance(mark, int) and 0 <= mark <= max_marks[i]):
                return f"{subjects[i]} marks should be between 0-{max_marks[i]}"

        total = sum(marks)

        # Pass/Fail logic (simplified)
        if all(mark >= 23 for mark in marks[:3] + marks[4:]) and maths >= 27 and english >= 27:
            pass_fail = 'P'
        else:
            pass_fail = 'F'

        query = ("INSERT INTO exam (Admin_no, Physics, Chemistry, English, CS, Hindi, Maths, Bio, Total, Pass_Fail) "
                 "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data = (admin_no, physics, chemistry, english, cs, hindi, maths, biology, total, pass_fail)
        self.cu.execute(query, data)
        self.con.commit()
        return "Marks added successfully!"

    def get_exam_result(self, admin_no=None, class_=None):
        if admin_no:
            self.cu.execute(f"SELECT * FROM exam WHERE Admin_no={admin_no}")
            return self.cu.fetchone()
        elif class_:
            # Assuming class is stored in student table
            self.cu.execute(f"SELECT e.* FROM exam e JOIN student s ON e.Admin_no = s.Admin_no WHERE s.Class={class_}")
            return self.cu.fetchall()
        else:
            self.cu.execute("SELECT * FROM exam")
            return self.cu.fetchall()

    def delete_student(self, admin_no):
        if not self.check_ele("exam", admin_no):
            return "Student marks do not exist"

        self.cu.execute(f"DELETE FROM exam WHERE Admin_no={admin_no}")
        self.cu.execute(f"DELETE FROM student WHERE Admin_no={admin_no}")
        self.con.commit()
        return "Student deleted successfully"

    def get_all_students(self):
        self.cu.execute("SELECT * FROM student")
        return self.cu.fetchall()