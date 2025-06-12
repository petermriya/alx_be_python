class Student:
    def __init__ (self, height, age, grade, name):
        self.height = height
        self.age = age
        self.grade = grade
        self.name = name
    
    def display_info (self):
        print (f"Student name: {self.name}")
        print (f"Student age: {self.age}")

student1 = Student(20, 15, "A", "Peter")

student1.display_info()
