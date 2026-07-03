# create student class that takes name and marks of 3 subjects as argument in constructor and create a method to print the average marks of the student.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # marks should be a list of 3 subjects

    def average_marks(self):
        Avg = sum(self.marks) / len(self.marks)
        print("hi", self.name, "your average score is:", Avg)
    
# Example usage:
student1 = Student("John", [98, 99, 100])
student1.average_marks()

student2 = Student("Alice", [94, 95, 96])
student2.average_marks()