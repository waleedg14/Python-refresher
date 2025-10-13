# ------ex 1
friend_ages = {"Rolf":  24, "Adam":30, "Anee":  27}

friend_ages["Rolf"] =20

print(friend_ages)

# ------ ex 2
friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27},
    ]

print(friends)
print(friends[1]["name"])

# ------ ex 3 - Iteration
student_attendance = {"Rolf":  96, "Adam":80, "Anee":  100}

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")

# Better

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

# -- Using the `in` keyword --

if "Bob" in student_attendance:
    print(f"Bob: {student_attendance[student]}")
else:
    print("Bob isn't a student in this class!")

# -- Calculate an average with `.values()` --

attendace_values = student_attendance.values()
print(sum(attendace_values) / len(attendace_values))