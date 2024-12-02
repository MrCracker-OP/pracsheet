# Create an empty dictionary
student_marks = {}

# Take the number of students and their marks as input
num_students = int(input("Enter the number of students: "))

for _ in range(num_students):
    name = input("Enter student name: ")
    marks = int(input(f"Enter marks for {name}: "))
    student_marks[name] = marks

# Calculate and display the average marks
total_marks = sum(student_marks.values())
average_marks = total_marks / num_students
print(f"Average marks: {average_marks:.2f}")

# Display the student with the highest and lowest marks
highest_marks_student = max(student_marks, key=student_marks.get)
lowest_marks_student = min(student_marks, key=student_marks.get)

print(f"Student with highest marks: {highest_marks_student} ({student_marks[highest_marks_student]})")
print(f"Student with lowest marks: {lowest_marks_student} ({student_marks[lowest_marks_student]})")

# Update the dictionary by adding a new student's marks and display the updated dictionary
new_student_name = input("Enter the new student name: ")
new_student_marks = int(input(f"Enter marks for {new_student_name}: "))
student_marks[new_student_name] = new_student_marks

print("Updated dictionary of student marks:")
print(student_marks)
