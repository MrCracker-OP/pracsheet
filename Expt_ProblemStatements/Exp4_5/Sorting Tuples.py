# Create a list of tuples where each tuple contains a person's name and age
people = [
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 35),
    ("David", 20)
]

# Sort the list of tuples by age in ascending order
# Convert each tuple to (age, name) for sorting by age
people_by_age = [(age, name) for name, age in people]
people_by_age.sort()  # Sort by age because age is the first element in the tuple

# Convert back to (name, age) tuples
people_sorted_by_age = [(name, age) for age, name in people_by_age]

# Display the sorted list by age
print("Sorted by age:")
for person in people_sorted_by_age:
    print(person)

# Sort the list of tuples by name in alphabetical order
# Convert each tuple to (name, age) for sorting by name
people_by_name = [(name, age) for name, age in people]
people_by_name.sort()  # Sort by name, name is the first element

# Display the sorted list by name
print("\nSorted by name:")
for person in people_by_name:
    print(person)
