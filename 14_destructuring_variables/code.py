t = 5, 11
x, y = t

print(x, y)


# -------2
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

print(list(student_attendance.items()))

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

# -----ex 3 this one isn't clear example

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Teacher")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

#--------------  ex 4
person = ("Bob", 42, "Mechanic")
name, _, profession = person

print(name, profession)

#--------------  ex 5
head, *tail = [1, 2, 3, 4, 5]
*head, tail = [1, 2, 3, 4, 5]
print(head)
print(tail)