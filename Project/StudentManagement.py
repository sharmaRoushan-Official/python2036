# Student Record System	Add, view, search, update, and delete student records stored in a file.
class Student:
    fileName = "student.txt"

    def __init__(self,student_id,name,age,course,marks):
        self.student_id = student_id
        self.name = name 
        self.age = age 
        self.course = course
        self.marks = marks

    # Calculate Grade
    def calculate_greade(self):
        if self.marks>=90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks>=70:
            return "B"
        elif self.marks>=60:
            return "C"
        else:
            return "D"
    # Convert object data into file format
    def to_file_format(self):
        return f"{self.student_id}|{self.name}|{self.age}|{self.course}|{self.marks}\n"
    ### Display Student details
    def display(self):
        print("_"*50)
        print(f"Student ID : {self.student_id}")
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")
        print(f"Student Course:{self.course}")
        print(f"Student Marks:{self.marks}")
        print("_"*50)


class StudentRecordSystem:
    # Add Student

    def add_student(self):
        print("\n===== ADD STUDENT =====")
        student_id = input("Enter Student ID: ")



    
