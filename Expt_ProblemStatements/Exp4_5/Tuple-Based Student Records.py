# Create a list of tuples where each tuple contains a student's name, age, and marks
students_tuples = [
    ("Alice", 20, 85),
    ("Bob", 22, 90),
    ("Charlie", 21, 78),
    ("David", 23, 88)
]

# Convert the list of tuples into a dictionary
students_dict = {}
for name, age, marks in students_tuples:
    students_dict[name] = {'age': age, 'marks': marks}

# Display the student records
print("Student Records:")
for name, info in students_dict.items():
    print(f"{name}: Age = {info['age']}, Marks = {info['marks']}")

