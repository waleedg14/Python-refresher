# part 1
student = {"name": "Waleed", "grades": (89, 90, 93, 78, 90)}

def average(sequence):
    return sum(sequence) / len(sequence)

print(average(student["grades"]))

# part 2
class Student:
    # init is a method because it's in a class
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades  # use the grades passed in

    # average is now correctly indented as a method of Student
    def average(self):
        return sum(self.grades) / len(self.grades)

# Create instances of Student
student = Student("Bob", (100, 100, 93, 78, 90))
student2 = Student("Rolf", (90, 90, 93, 78, 90))

# Print the average grade
print(student.name)
print(student.average())
print(student2.average())
